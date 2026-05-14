from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import RegisterForm


def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):

    form = RegisterForm(request.POST or None)

    if form.is_valid():

        user = form.save(commit=False)

        user.set_password(form.cleaned_data['password'])

        user.is_staff = False

        user.save()

        return redirect('login')

    return render(request, 'users/register.html', {'form': form})