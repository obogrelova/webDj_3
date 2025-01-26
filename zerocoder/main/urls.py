from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('newpage2', views.newpage2, name='page2'),
    path('newpage3', views.newpage3, name='page3'),
    path('newpage4', views.newpage4, name='page4')
]