from django.urls import path
from accounts import views
from todo.views import create_todo, delete_todo, index, todos, update_todo, complete_todo

urlpatterns = [
    # path('', views.Todos, name="todo_list"),
	path('', todos, name="todos"),
	path('index/', index),
	path('create_todo/', create_todo, name="create"),
	path('update_todo/<int:pk>/', update_todo, name='update'),
	path('delete_todo/<int:pk>/', delete_todo, name='delete'),
	path('complete_todo/<int:pk>/', complete_todo, name='complete'),
]