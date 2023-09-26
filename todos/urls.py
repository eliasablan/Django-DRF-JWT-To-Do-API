from django.urls import path

from .views import TodoList

urlpatterns = [
    path('', TodoList.as_view(), name='todo-list'),
]