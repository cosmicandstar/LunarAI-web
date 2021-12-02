from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video', views.video, name='video'),
    path('upload', views.upload, name='upload'),
    path('train', views.train, name='train')
]
