from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'queue/index.html')

def add(request):
    return render(request, 'queue/add.html')

def vote(request):
    return render(request, 'queue/vote.html')
