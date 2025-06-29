from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # root URL redirect karega
    path('remove-background/', views.background_remover, name='remove_bg'),
    path('enhance-image/', views.image_enhancer, name='enhance_image'),  
]
