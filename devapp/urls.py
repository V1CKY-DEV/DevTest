from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_file, name='upload_file'),  # Ensure this path matches the FilePond server URL
    path('success/', views.success, name='success'),
]
