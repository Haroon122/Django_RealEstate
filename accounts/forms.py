from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from contacts.models import Contact

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class AdminSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    is_staff = forms.BooleanField(initial=True, widget=forms.HiddenInput())
    is_superuser = forms.BooleanField(initial=True, widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'is_superuser')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('listing', 'listing_id', 'name', 'email', 'phone', 'message',) 