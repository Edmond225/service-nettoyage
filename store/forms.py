from django import forms
from .models import DemandeDevis

class DemandeDevisForm(forms.ModelForm):
    class Meta:
        model = DemandeDevis
        fields = ['nom', 'email', 'telephone', 'logement', 'message']  # <-- ajouter 'telephone'
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'Votre nom'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Votre email'}),
            'telephone': forms.TextInput(attrs={'placeholder': 'Votre numéro de téléphone'}),
            'logement': forms.Select(),
            'message': forms.Textarea(attrs={'placeholder': 'Votre message...', 'rows':4}),
        }
