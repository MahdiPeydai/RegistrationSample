from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate
from django.contrib import messages
from .authentication import admin_authentication


class RegistrationView(APIView):
    def get(self, request):
        reg_form = UserRegisterForm()
        login_form = UserLoginForm
        return render(request, 'authentication/authentication.html',
                      {'reg_form': reg_form, 'login_form': login_form, 'default': 'registration'})

    def post(self, request):
        reg_form = UserRegisterForm(request.POST)
        if reg_form.is_valid():
            return redirect('login')
        else:
            login_form = UserLoginForm
            return render(request, 'authentication/authentication.html',
                          {'reg_form': reg_form, 'login_form': login_form, 'default': 'registration'})


class LoginView(APIView):
    def get(self, request):
        login_form = UserLoginForm()
        reg_form = UserRegisterForm
        return render(request, 'authentication/authentication.html',
                      {'reg_form': reg_form, 'login_form': login_form, 'default': 'login'})

    def post(self, request):
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                if admin_authentication(user):
                    return
                else:
                    messages.error(request, 'شما به پنل دسترسی ندارید')
                    return redirect('login')
            else:
                messages.error(request, 'ایمیل یا رمز عبور صحیح نمی‌باشد')
                return redirect('login')
        else:
            messages.error(request, 'ایمیل یا رمز عبور صحیح نمی‌باشد')
            return redirect('login')

