from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .forms import UserRegisterForm, UserLoginForm


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


