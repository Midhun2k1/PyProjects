from django.urls import path

from SchoolApp import views

app_name = "SchoolApp"

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('form/', views.form_submission, name="form"),
]
