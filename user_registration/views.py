from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    form = UserForm(request.POST)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = UserForm()
    else:
            form = UserForm()
    context = {
        'form':form,
    }
    return render(request, 'user_registration/register.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None and user.is_staff:
            if user.is_active:
                login(request,user) 
                return redirect('index')
            else:
                messages.error(request, 'Account is not active')
                return render(request, 'user_registration/login.html')

        elif user is not None and not user.is_staff:
            if user.is_active:
                login(request,user)
                return redirect('index-about')
            else:
                messages.warning(request, 'Account is not active')
                return render(request, 'user_registration/login.html')
        
        else:
            messages.error(request, 'Please enter valid details')
            return render(request, 'user_registration/login.html')

    context = {}
    return render(request, 'user_registration/login.html', context)
@login_required
def logout_view(request):
    logout(request)
    return redirect('login-page')