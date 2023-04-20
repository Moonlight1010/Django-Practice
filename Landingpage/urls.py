from django.urls import path
from .views import index, about, notification, read, update, delete_view

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name='index-about'),
    path('notification/', notification, name='index-notification'),
    path('read/<int:id>', read, name='read-page'),
    path('update/<int:id>', update, name='update-page'),
    path('delete/<int:id>', delete_view, name='delete'),
]