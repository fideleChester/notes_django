from django.forms import ModelForm
from .models import Note,Eleve
from django import forms

class NoteForm(ModelForm):
    valeur = forms.FloatField(min_value=0, max_value=20, label="Note sur 20")
    class Meta:
        fields = ['valeur']
        model = Note
        labels = {"valeur":"Note sur 20"}
        
        
class EleveForm(ModelForm):
    """ nom = forms.CharField(max_length=20, label="Nom")
    prenom = forms.CharField(max_length=20, label="Prénom")
    niveau = forms.CharField(max_length=20, label="Niveau")
    date_naissance = forms.DateField(label="Date de naissance")
    sexe = forms.CharField(max_length=1, label="Sexe", choices=(("M", "Masculin"), ("F", "Féminin")))
    id = forms.IntegerField(label="ID") """
    
    class Meta:
        fields = "__all__"
        model = Eleve
        


    
