from django.shortcuts import render

def home(request):
    return render(request, 'todo/home.html', {})

def login(request):
    return render(request, 'todo/login.html', {})

def register(request):
    return render(request, 'todo/register.html', {})