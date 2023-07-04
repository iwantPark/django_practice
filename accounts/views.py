from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, SignInForm  # .forms 경로에서 작성한 패키지를 불러옴
from django.contrib import messages

def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')  # Redirect to the login page after successful registration
        
    return render(request, 'accounts/signup.html', {'form': form})
        
def signin(request):
    if request.method == 'GET':
        form = SignInForm()
    elif request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('todo_list')  # Redirect to the home page after successful login
            else:
                messages.error(request)
            
    return render(request, 'accounts/signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('signin')