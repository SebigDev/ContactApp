from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .forms import ContactAppUser, UserCreationForm, User


def register(request):
    if request.method == 'POST':
        form = ContactAppUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('success_reg')
    else:
        form = ContactAppUser()
    return render(request, 'registration/register.html', {'form': form})



