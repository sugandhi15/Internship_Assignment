from django.urls import path,include
from . import views

urlpatterns = [
    path('hello', views.hello_view.as_view()),
    path('register/', views.registration.as_view()),
    path('login/', views.login.as_view()),
    path('profile/', views.information.as_view()),
]