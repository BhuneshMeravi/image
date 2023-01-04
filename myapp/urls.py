from django.urls import path
from . import views

urlpatterns = [
    path('image/', views.image, name='image'),
]
# The thumbnail, medium, large, and grayscale versions of the image will be saved to your Django storage backend