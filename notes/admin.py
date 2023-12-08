from django.contrib import admin
from .models import Niveau,Eleve,Enseignant,Matiere,Note
from .forms import EleveForm
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class NiveauAdmin(ImportExportModelAdmin):
    list_display = ["nom"]
    
admin.site.register(Niveau,NiveauAdmin)
  
class EleveAdmin(ImportExportModelAdmin):
    list_display = ["nom","prenom","niveau","sexe"]
    list_per_page = 10
    search_fields = ["nom","prenom"]
    list_filter = ["niveau"]
    form = EleveForm
    
admin.site.register(Eleve,EleveAdmin)

class EnseignantAdmin(ImportExportModelAdmin):
    list_display = ["nom","prenom","sexe"]

admin.site.register(Enseignant,EnseignantAdmin)

class MatiereAdmin(ImportExportModelAdmin):
    list_display = ["nom"]
    
admin.site.register(Matiere,MatiereAdmin)

class NoteAdmin(ImportExportModelAdmin):

    list_per_page = 10

    list_filter = ["eleve__niveau"]
admin.site.register(Note,NoteAdmin)

