from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('upload/', views.upload_image, name='upload'),
    path('api/upload/', views.upload_image_api, name='upload_api'),
    path('delete/<int:pk>/', views.delete_image, name='delete_image'),
    path('api/', views.api_instructions, name='api_instructions'),  # Add this line
    path('i18n/', include('django.conf.urls.i18n')),
]