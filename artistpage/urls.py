from django.urls import path
from . import views

urlpatterns = [
    path('', views.artpage, name='artistpage/artpage'),  # maps /artistpage/
]
