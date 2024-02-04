from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    ## Model Meta is basically the inner class of your model class. Model Meta is basically used to change the behavior of your model fields like changing order options,verbose_name, and a lot of other options. It's completely optional to add a Meta class to your model.
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'password' : forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
        }
        