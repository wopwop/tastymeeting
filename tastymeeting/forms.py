# Froms class
# -*- coding: utf-8 -*-

from django import forms
from tastymeeting.models import Profile

class signupForm(forms.Form):
    first_name = forms.CharField(error_messages = {'required':'Votre prénom est obligatoire.'})
    last_name = forms.CharField(error_messages = {'required':'Votre nom est obligatoire.'})
    email = forms.EmailField(error_messages = {'required':'Votre adresse email est obligatoire.','invalid':'Entrez une adresse email valide.'})
    password = forms.CharField(error_messages = {'required':'Le mot de passe est obligatoire.'})
    
class loginForm(forms.Form):
    email = forms.EmailField(error_messages = {'required':'Votre adresse email est obligatoire.','invalid':'Entrez une adresse email valide.'})
    password = forms.CharField(error_messages = {'required':'Le mot de passe est obligatoire.'})
    
class profileForm(forms.ModelForm):
    first_name = forms.CharField(error_messages = {'required':'Votre prénom est obligatoire.'})
    last_name = forms.CharField(error_messages = {'required':'Votre nom est obligatoire.'})
    image = forms.ImageField(error_messages = {'invalid_image':"Ajouter une image valide. Le fichier que vous avez téléchargé soit n'était pas une image ou une image corrompue."})
    class Meta:
        model = Profile
        exclude = ('user',)