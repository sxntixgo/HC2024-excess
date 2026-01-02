from django.db import connection
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, render
from .models import Attempt


from datetime import datetime, timezone, timedelta
from os import getenv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import FirefoxOptions
import threading
import signal


WAIT_TIME = int(getenv('WAIT_TIME', '5'))

class GameUserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'server/gameuser_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        #save the new user first
        form.save()
        #get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        #authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)

class AttemptDetailView(LoginRequiredMixin, DetailView):
    model = Attempt

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class AttemptListView(LoginRequiredMixin, ListView):
    model = Attempt
    paginate_by = 25
    ordering = ['-datetime']

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class AttemptCreateView(LoginRequiredMixin, CreateView):
    model = Attempt
    fields = ['target_server', 'resource_and_query_string']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["wait_time"] = WAIT_TIME
        return context

    def form_valid(self, form):
        user = get_object_or_404(User, pk=self.request.user.pk)
        if user.gameuser.last_check:
            if (datetime.now(timezone.utc) - user.gameuser.last_check) < timedelta(minutes=WAIT_TIME):
                return HttpResponseRedirect('wait')
        user.gameuser.last_check = datetime.now(timezone.utc)
        user.save()
        form.instance.user = user
        response = super().form_valid(form)
        t = threading.Thread(target=check_payload, args=(self.object,))
        t.start()
        return response
    
def render_wait(request):
    return render(request, "server/wait.html", {'wait_time': WAIT_TIME})
    
def check_payload(attempt):
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(options=firefox_options)

    try:    
        driver.get(attempt.target_server.url+attempt.resource_and_query_string)
        WebDriverWait(driver,5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        attempt.result = True
    except:
        attempt.result = False
    finally:
        attempt.completed = True
        attempt.save()
        connection.close()
        driver.close()