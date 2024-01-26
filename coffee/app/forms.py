
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User 
from .models import client 

class LoginForm(AuthenticationForm):
    nom = UsernameField(widget = forms.TextInput (attrs={'autofocus':'True','Class':'form-control'  }))
    password = forms.CharField(widget=forms.PasswordInput ({'autofocus' :'True','class':'form-control' }  ))


class CustomerRegistrationForm(UserCreationForm):
    nom = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    motdepasse1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    motdepasse2 = forms.CharField(label='Confirmer mot de passe', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class Meta :
    model = User 
    fields = ['username','email','password1','password']  

class MyPasswordResetForm (PasswordChangeForm):
  pass



from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User 

class LoginForm(AuthenticationForm):
    nom = UsernameField(widget = forms.TextInput (attrs={'autofocus':'True','Class':'form-control'  }))
    password = forms.CharField(widget=forms.PasswordInput ({'autofocus' :'True','class':'form-control' }  ))


class CustomerRegistrationForm(UserCreationForm):
    nom = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    motdepasse1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    motdepasse2 = forms.CharField(label='Confirmer mot de passe', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class Meta :
    model = User 
    fields = ['username','email','password1','password']  

class MyPasswordResetForm (PasswordChangeForm):
  pass


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = client
        fields = ['nom', 'localisation', 'ville', 'telephone', 'province']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'localisation': forms.TextInput(attrs={'class': 'form-control'}),
            'ville': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.NumberInput(attrs={'class': 'form-control'}),
            'province': forms.Select(attrs={'class': 'form-control'}),
        }