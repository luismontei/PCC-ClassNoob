from django.shortcuts import render,  reverse
from django.shortcuts import redirect
from django.contrib import auth
from .forms import CustomUserForm
from django.urls import reverse_lazy
from django.views import generic


def register(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/accounts/login")
    else:
        form = CustomUserForm()

    context = {
        'form': form
    }

    return render(request, 'registration/login.html', context)

def sair(request):
    auth.logout(request)
    return redirect('/accounts/login/')