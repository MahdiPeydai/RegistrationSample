from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="نام", max_length=50, min_length=4,
                                 widget=forms.TextInput(attrs={"placeholder": "نام", 'class': 'form-control'}),
                                 required=True)
    last_name = forms.CharField(label="نام خانوادگی", max_length=50, min_length=4,
                                widget=forms.TextInput(attrs={"placeholder": "نام خانوادگی", 'class': 'form-control'}),
                                required=False)
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(attrs={"placeholder": "ایمیل", 'class': 'form-control'}))
    phone = forms.CharField(label="شماره همراه", max_length=11,
                            widget=forms.TextInput(attrs={"placeholder": "شماره همراه: ", 'class': 'form-control'}),
                            validators=[RegexValidator(
                                regex=r'^09\d{9}$',  # Pattern for Iranian phone number format
                                message='شماره تماس صحیح 09106956260',
                                code='invalid_phone_number'
                            )],
                            required=True)
    password1 = forms.CharField(label="رمز عبور",
                                widget=forms.PasswordInput(attrs={"placeholder": "رمز عبور", 'class': 'form-control'}),
                                required=True)
    password2 = forms.CharField(label="تکرار رمز عبور", required=True,
                                widget=forms.PasswordInput(attrs={"placeholder": "تکرار رمز عبور", 'class': 'form-control'}))

    error_messages = {'password_mismatch': "رمز عبور تایید نشد"}

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match. Please enter matching passwords for New Password and Confirm New Password.")

        return cleaned_data

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone']


class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(attrs={"placeholder": "ایمیل", 'class': 'form-control'}), required=True)
    password = forms.CharField(label="رمز عبور", widget=forms.PasswordInput(attrs={"placeholder": "رمز عبور", 'class': 'form-control'}),
                               required=True)
