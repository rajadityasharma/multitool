from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # root URL redirect karega
    path('remove-background/', views.background_remover, name='remove_bg'),
    path('enhance-image/', views.image_enhancer, name='enhance_image'), 
    path('compress-image/', views.image_compressor, name='compress_image'),
    path('image-to-pdf/', views.image_to_pdf, name='image_to_pdf'),
]
