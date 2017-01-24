# _*_ coding: utf-8 _*_
import re
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class FormularzWizytowka(forms.Form):
    uczelnia = forms.CharField(label="Nazwa uczelni:",max_length=120)
    kierunek = forms.CharField(label="Kierunek studiów:",max_length=60)
    telefon = forms.CharField(label="Telefon:",max_length=15)

class FormularzRejestracji(forms.Form):
    username = forms.CharField(label="Login:",max_length=30)
    email = forms.EmailField(label="Email:")
    password1 = forms.CharField(label="Hasło:",widget=forms.PasswordInput())
    password2 = forms.CharField(label="Powtórz hasło:",widget=forms.PasswordInput())
    first_name = forms.CharField(label="Imię:", max_length=50)
    last_name = forms.CharField(label="Nazwisko:", max_length=50)
    log_on = forms.BooleanField(label="Logowanie po rejestracji:",required=False)
    
    
    def clean_password2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        if password1==password2:
            return password2
        else:    
            raise forms.ValidationError("Hasła muszą być takie same")
            
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$',username):
            raise forms.ValidationError("Login może składać się tylko z cyfr i liter")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Taki użytkownik już istnieje")
        
class FormularzLogowania(forms.Form):
    username = forms.CharField(label="Login:",max_length=30)
    password = forms.CharField(label="Hasło:",widget=forms.PasswordInput())
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
            return username
        except ObjectDoesNotExist:
            raise forms.ValidationError("Niepoprawny login")   
            
    def clean_password(self):
        if self.cleaned_data.has_key('username'):
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            user = User.objects.get(username=username)
            if user.check_password(password):
                return password
            raise forms.ValidationError("Niepoprawne hasło")                
