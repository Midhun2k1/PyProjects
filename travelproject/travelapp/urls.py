from django.urls import path

from travelapp import views

urlpatterns = [
    path('', views.demo, name='demo'),
    # path('', views.passi, name='passi'),
    # path('add/',views.addition,name="addition"),
    # path('about/',views.about, name='about'),
    # path('mim/',views.mim, name='mim'),
]
