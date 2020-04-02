"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #auth
    #registration
    path('signup/', views.signupuser, name='signupuser'),
    #login
    path('login/', views.loginuser, name='loginuser'),
    #logout
    path('logout/', views.logoutuser, name='logoutuser'),

    #todos
    #todos displaying
    path('curent/', views.curenttodos, name='curenttodos'),
    #todos completed
    path('completed/', views.completedtodos, name='completedtodos'),
    #create todo
    path('create/', views.createtodo, name='createtodo'),
    #homepage
    path('', views.home, name='home'),
    #todo edit
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    #todo complate
    path('todo/<int:todo_pk>/complate', views.complatetodo, name='complatetodo'),
    #todo delate
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),
]
