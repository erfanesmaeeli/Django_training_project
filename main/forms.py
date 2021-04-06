from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(forms.Form):
	username = forms.CharField(label="نام کاربری", max_length=15, required=True, help_text="از حروف فارسی استفاده نکنید!",
	widget=forms.TextInput(attrs={'placeholder': 'example: ali'})
	)
	password = forms.CharField(label="رمز عبور", min_length=8, widget=forms.PasswordInput)



class SignUpForm2(UserCreationForm):
	phone = forms.CharField(max_length=15, required=True, label="تلفن همراه", help_text="همراه با صفر وارد کنید")
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'phone', 'email', 'password1', 'password2')