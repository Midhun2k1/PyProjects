from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.add, name="add"),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/', views.Tasklistview.as_view(), name='cbvhome'),
    path('details/<int:pk>/', views.Tastdetailview.as_view(), name='details'),
    path('cbvedit/<int:pk>/', views.Taskupdateview.as_view(), name='cbvedit'),
    path('cbvdelete/<int:pk>/', views.Taskdeleteview.as_view(), name='cbvdelete'),
]
