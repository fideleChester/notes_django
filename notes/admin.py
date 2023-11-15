from django.contrib import admin
from .models import Niveau,Eleve,Enseignant,Matiere,Note
# Register your models here.
class NiveauAdmin(admin.ModelAdmin):
    list_display = ["nom"]
    
admin.site.register(Niveau,NiveauAdmin)
  
class EleveAdmin(admin.ModelAdmin):
    list_display = ["nom","prenom","niveau",'id']
    
admin.site.register(Eleve)

class EnseignantAdmin(admin.ModelAdmin):
    list_display = ["nom","prenom","sexe"]

admin.site.register(Enseignant)

class MatiereAdmin(admin.ModelAdmin):
    list_display = ["nom"]
    
admin.site.register(Matiere)

class EleveAdmin(admin.ModelAdmin):
    list_display = ["valeur","matiere"]
admin.site.register(Note,EleveAdmin)
