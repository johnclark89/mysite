from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from models import Commande, CommandePizza
from django.forms import ModelForm

# Personnalisation du formulaire d'enregistrement du client
class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        # import du model de base
        model = User
        # ordre des champs
        fields = ('username', 'last_name', 'first_name', 'email', 'password1', 'password2')
    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# Formulaire du model Commande
class CommandeForm(ModelForm):
    class Meta:
        # import du model de base
        model = Commande

# Formulaire du model CommandePizza
class CommandePizzaForm(ModelForm):
    class Meta:
        # import du model de base
        model = CommandePizza

