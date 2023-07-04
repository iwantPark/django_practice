from django.shortcuts import get_object_or_404, redirect, render
import todo
from todo.models import TodoList
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from todo.models import TodoList

#완료기능 추가
def complete_todo(request, pk):
    curTodo = get_object_or_404(TodoList, pk=pk)
    curTodo.complete = True
    curTodo.save()
    return redirect('todos')

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

class TodoCreate(LoginRequiredMixin, CreateView): #LoginRequiredMixin을 사용하였기 때문에
    model = todo	#로그인이 필요함. 하지만 로그인 되지 않았다면
    fields = ['todo', 'description', 'important'] #login_url로 이동하도록 함.
    login_url = '/accounts/signin/' #기본 설정은 다르게 되어있어서 직접 지정해주어야 함

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