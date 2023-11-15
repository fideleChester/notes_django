from django.shortcuts import render,get_object_or_404
from .models import Eleve,Matiere,Niveau
from django.http import Http404
from django.db.models import Avg

#Mes modules
from .methodes.methods_eleve import *
# Create your views here.
def index(request):
    return render(request, 'notes/index.html')

#La vue de tous les eleves



def eleves(request):
    eleves  = Eleve.objects.all()
    return render(request, 'eleves/index.html', {'eleves': eleves})

#Les détails de chaque eleve
def eleve(request, id):
    try:
        # La moyenne de cet éléve rangée dans le tableau
        
        eleve = Eleve.objects.get(id=id)
        matieres = eleve.niveau.matiere_set.all()   
        # Calcul de la moyenne de chaque matière
        moyennes =  calcul_moyenne_eleve_par_matiere(matieres)
        
        moyennne_generale = moyenne_generale_eleve(moyennes)
        
        context = {
            'eleve': eleve,
            'matieres':zip(moyennes,matieres),
            "moyennes":moyennes,
            "moyenne_generale":moyennne_generale
        }
        
    except Eleve.DoesNotExist:
        raise Http404("Cet eleve n'existe pas")
       
    return render(request, 'eleves/details.html',context )

#La vue des matieres
def matieres(request):
    matieres = Matiere.objects.all()
    return render(request, 'matieres/index.html', {'matieres': matieres})

#details d'une matiere
def matiere(request, id):
    details = get_object_or_404(Matiere, id=id)
    return render(request, 'matieres/details.html', {'details': details})

#les détails de chaque niveau
def niveau(request, id):
    details = get_object_or_404(Niveau, id=id)
    return render(request, 'niveaux/details.html', {'details': details})