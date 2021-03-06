from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import UserLoginForm, UserRegistrationForm
from .models import User


def user_login(request):
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request, email=cd['email'], password=cd['password'])
			if user is not None:
				login(request, user)
				messages.success(request, 'با موفقیت وارد شدید', 'success')
				return redirect('shopping:home')
			else:
				messages.error(request, 'ایمیل یا گذرواژه نادرست است', 'danger')
	else:
		form = UserLoginForm()
	return render(request, 'accounts/login.html', {'form':form})


def user_logout(request):
	logout(request)
	messages.success(request, 'با موفقیت خارج شدید', 'success')
	return redirect('shopping:home')


def user_register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = User.objects.create_user(cd['email'], cd['first_name'], cd['last_name'], cd['password'])
			user.save()
			messages.success(request, 'ثبت‌نام شما با موفقیت انجام شد', 'success')
			return redirect('shopping:home')
	else:
		form = UserRegistrationForm()
	return render(request, 'accounts/register.html', {'form':form})
