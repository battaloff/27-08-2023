
from django.contrib import admin
from django.urls import path
from table import views

urlpatterns = [
    # Admin page
    path('admin/', admin.site.urls),
    # Home page
    path('', views.home, name='home'),

    path('update_task_status/', views.update_task_status, name='update_task_status'),


]
