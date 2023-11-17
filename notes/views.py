from django.shortcuts import redirect, render,get_object_or_404,HttpResponse
from .models import Eleve,Matiere,Niveau,Note
from django.http import Http404


#Mes modules
from .methodes.methods_eleve import *
# Create your views here.
def index(request):
    return render(request, 'base.html')

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





def add_note(request,eleve,matiere):
    if request.method == 'POST':
        note = request.POST['note']
        eleve = Eleve.objects.get(id=eleve)
        """
            La methode pour verifier si l'élève suit la matiere, True si vrai
        """
        eleve_suit_matiere = verifie_eleve_suit_matiere(eleve=eleve,matiere=matiere)
        
        if not eleve_suit_matiere:
            raise Http404("Cet eleve ne suit pas cette matiere")
        else:
            sav_note = Note(valeur=note,eleve_id=eleve.id,matiere_id=matiere)
            sav_note.save()
            """
            On redirige vers les détails de l'élève
            """
            return redirect('notes:eleve',id=eleve.id)
    return render(request, 'notes/add_note.html')