"""
Definition of forms.
"""

from django import forms
from django.forms import widgets, ModelForm
from psw.models import Commands, Services
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _


        
class pswAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Nazwa uzytkownika'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Haslo'}))

class pswCreateForm(UserCreationForm):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Nazwa użytkownika'}))
    first_name = forms.CharField(max_length=30,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Imię'}))
    last_name = forms.CharField(max_length=30,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Nazwisko'}))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput({
                                 'class': 'form-control',
                                 'placeholder': 'Adres Email'}))
    password1 = forms.CharField(label=("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Hasło'}))
    password2 = forms.CharField(label=("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Powtórz Hasło'}))
    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2')

    def save(self,commit = True):   
        user = super(pswCreateForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user

class CommandForm(forms.ModelForm):
    IP_CHOICES = (('192.168.0.10','192.168.0.10'),('192.168.0.11','192.168.0.11'))
    SYSTEM_CHOICES = (('Ubuntu','Ubuntu'),('Debian','Debian'))
    RAM_CHOICES = (('64','64'),('128','128'),('256','256'))
    QUOTE_CHOICES = (('5','5'),('10','10'),('15','15'))
    #ip = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=IP_CHOICES)
    system = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=SYSTEM_CHOICES)
    ram = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=RAM_CHOICES)
    quote = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=QUOTE_CHOICES)
    name = forms.CharField(max_length=8, widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Commands
        fields = ('system','ram','quote','name')




class ServicesForm(forms.ModelForm):
    
        
    SQL_CHOICES = (('mySQL','mySQL'),('PostreSQL','PostgreSQL'))
    HTTP_CHOICES = (('Apache2','Apache2'),('Nginx','Nginx'))
    PHP_CHOICES = (('5.3','5.3'),('5.4','5.4'),('5.5','5.5'))
    contener = forms.ModelChoiceField(queryset = Commands.objects.none() ,widget=forms.Select(attrs={'class':'form-control'}))
    sql = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=SQL_CHOICES)
    http = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=HTTP_CHOICES)
    php = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=PHP_CHOICES)
    class Meta:
        model = Services
        fields = ('contener','sql','http','php')
  
          
    def __init__(self, *args, **kwargs):
        
        user = kwargs.pop('user',None)
        super(ServicesForm, self).__init__(*args, **kwargs)
        qs = Commands.objects.filter(user=user)
        self.fields['contener'].initial = qs
        self.fields['contener'].queryset = qs     
      
    
        
           
