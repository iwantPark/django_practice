from django.shortcuts import get_object_or_404, redirect, render
from todo.models import TodoList

# Create your views here.
from django.shortcuts import render
from todo.models import TodoList

# Create your views here.

def delete_todo(request, pk):
	delTodo = get_object_or_404(TodoList, pk=pk)
	delTodo.delete()
	return redirect('todos')

def update_todo(request, pk):
	curTodo = get_object_or_404(TodoList, pk=pk)
	if request.method == 'POST':
		curTodo.todo = request.POST['todo']
		curTodo.description = request.POST['description']
		curTodo.important = request.POST.get('important') == "on"
		curTodo.complete = request.POST.get('complete') == "on"
		curTodo.save()
		return redirect('todos')
	return render(
		request,
		'todo/todo_update.html',
		{
			'curTodo': curTodo,
		},
	)

def create_todo(request):
	myTodo = TodoList()
	if request.method == 'POST':
		myTodo.todo = request.POST['todo']
		myTodo.description = request.POST['description']
		myTodo.important = request.POST.get('important') == "on"
		myTodo.complete = request.POST.get('complete') == "on"
		myTodo.save()
		return redirect('todos')
	return render(
		request,
		'todo/todo_create.html'
	)

def todos(request):
	todolist = TodoList.objects.all()
	return render(
		request,
		'todo/todos.html',
        {
			'todolist': todolist,
		}
	)

def index(request):
	#todolist의 모든 레코드를 가져온다.
	todolist = TodoList.objects.all()
	return render(
		request,
		'todo/index.html',
		{
			#HTML에서 todolist라는 이름으로 todolist를 넘겨준다.
			'todolist': todolist,
		}
	)