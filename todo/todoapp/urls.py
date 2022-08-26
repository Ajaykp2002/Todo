from . import views
from django.urls import path

urlpatterns = [
    path('',views.task,name="task"),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('Listview/',views.TodoListview.as_view(),name='Listview'),
    path('detail/<int:pk>/',views.TodoDetailview.as_view(),name='detail'),
    path('update/<int:pk>/',views.TodoUpdateview.as_view(),name='update'),
    path('delete/<int:pk>/',views.TodoDeleteview.as_view(),name='delete'),
    ]