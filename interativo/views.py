from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def quiz(request):
    return render(request, 'quiz.html')

def final(request):
    return render(request, 'final.html')
