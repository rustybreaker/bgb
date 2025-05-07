from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def quiz(request):
    return render(request, 'quiz.html')

def menu(request):
    return render(request, 'menu.html')

def galeria(request):
    return render(request, 'galeria.html')  # ainda vamos criar esse template

def cartinha(request):
    return render(request, 'cartinha.html')

