from django.contrib import admin
from .models import Niveau,Eleve,Enseignant,Matiere
# Register your models here.

admin.site.register(Niveau)
admin.site.register(Eleve)
admin.site.register(Enseignant)
admin.site.register(Matiere)