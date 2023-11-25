from django import forms
from django.core.validators import RegexValidator

from Authentication.models import User


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label="نام", max_length=50, min_length=4,
                                 widget=forms.TextInput(attrs={"placeholder": "نام", 'class': 'form-control'}), required=True)
    last_name = forms.CharField(label="نام خانوادگی", max_length=50, min_length=4,
                                widget=forms.TextInput(attrs={"placeholder": "نام خانوادگی", 'class': 'form-control'}), required=True)
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(attrs={"placeholder": "ایمیل", 'class': 'form-control'}))
    phone = forms.CharField(label="شماره همراه", max_length=11,
                            widget=forms.TextInput(attrs={"placeholder": "شماره همراه: ", 'class': 'form-control'}),
                            validators=[RegexValidator(
                                regex=r'^09\d{9}$',  # Pattern for Iranian phone number format
                                message='شماره تماس صحیح 09106956260',
                                code='invalid_phone_number'
                            )],
                            required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone']
