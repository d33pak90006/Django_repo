from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('register')
    else:
        form = UserRegisterForm()
    return render(request, 'new_page/register.html', {'form': form})


def profile(request):
	return render(request,'new_page/profile.html')