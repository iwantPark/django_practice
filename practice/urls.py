from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')), #account 추가
    path('todo/', include('todo.urls')),
]
