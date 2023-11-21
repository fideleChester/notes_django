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
    
    class Meta:
        fields = "__all__"
        model = Eleve
        


    
