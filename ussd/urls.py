from django.urls import path
from ussd import views

urlpatterns = [
    path('', views.index,name='index')
]