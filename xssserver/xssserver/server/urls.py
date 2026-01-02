from django.contrib.auth import views as auth_views
from django.urls import path
from .views import AttemptCreateView, AttemptDetailView,AttemptListView, GameUserCreateView, render_wait

urlpatterns = [
    path('', AttemptCreateView.as_view(), name='home'),
    path('login', auth_views.LoginView.as_view(template_name='server/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('register', GameUserCreateView.as_view(), name='register'),
    path('attempts', AttemptListView.as_view(), name='attempts'),
    path('attempt/<str:pk>', AttemptDetailView.as_view(), name='attempt_detail'),
    path('wait', render_wait, name='wait')
]