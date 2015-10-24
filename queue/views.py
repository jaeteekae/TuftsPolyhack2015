from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def index(request):
    return render(request, 'queue/index.html')

@login_required
def add(request):
    return render(request, 'queue/add.html')

@login_required
def vote(request):
    return render(request, 'queue/vote.html')

def login(request):
    if (request.POST):
        if (request.POST.get('party_pw', '') != "PASSWORD"):
            print("fail")
            return render(request, 'queue/login.html')
        else:
            print("other fail")
            user = User.objects.get(username="generic_user")
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            auth_login(request, user)
            return HttpResponseRedirect('/queue')
    else:
        return render(request, 'queue/login.html')
