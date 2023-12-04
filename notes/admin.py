from django.contrib import admin
from .models import Niveau,Eleve,Enseignant,Matiere,Note
from .forms import EleveForm
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class NiveauAdmin(admin.ModelAdmin):
    list_display = ["nom"]
    
admin.site.register(Niveau,NiveauAdmin)
  
class EleveAdmin(ImportExportModelAdmin):
    list_display = ["nom","prenom","niveau","sexe"]
    list_per_page = 10
    search_fields = ["nom","prenom"]
    list_filter = ["niveau"]
    form = EleveForm
    
admin.site.register(Eleve,EleveAdmin)

class EnseignantAdmin(admin.ModelAdmin):
    list_display = ["nom","prenom","sexe"]

admin.site.register(Enseignant)

class MatiereAdmin(admin.ModelAdmin):
    list_display = ["nom"]
    
admin.site.register(Matiere)


admin.site.register(Note)
