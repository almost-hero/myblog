from django.shortcuts import render,redirect

from .forms import *

from django.contrib.auth import login,logout
# Create your views here.
def login_view(request):
    next = request.GET.get('next')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        login(request,user)
        if next:
            return redirect(next)
        return redirect('/')
    return render(request,'logsys/login_view.html',{'form':form})

def logout_view(request):
    next = request.GET.get('next')
    logout(request)
    if next:
        return redirect(next)
    return redirect('/')


def register_view(request):
    next = request.GET.get('next')
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit = False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username = user.username, password= password)
        login(request,new_user)
        if next:
            return redirect(next)
        return redirect('/')
    return render(request,'logsys/register_view.html',{'form':form})
