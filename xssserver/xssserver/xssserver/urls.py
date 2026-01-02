from django.contrib import admin
from django.urls import path, include
import os

urlpatterns = [
    path(os.getenv('DJANGO_ADMIN_URL')+'/', admin.site.urls),
    path('', include('server.urls'))
]