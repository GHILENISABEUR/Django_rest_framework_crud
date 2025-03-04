from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('drinks',views.drink_list,name="endpoint"),
    path('drinks/<int:id>/',views.drink_detail),
]