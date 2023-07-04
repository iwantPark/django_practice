from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"), # signup
    path('signin/', views.signin, name="signin"), # login
    path('logout/', views.signout, name='logout'), # logout
]