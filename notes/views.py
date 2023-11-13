from django.shortcuts import render,get_object_or_404
from .models import Eleve,Matiere,Niveau
from django.http import Http404
# Create your views here.
def index(request):
    return render(request, 'notes/index.html')

#La vue de tous les eleves
from .models import Eleve,Matiere
def eleves(request):
    eleves  = Eleve.objects.all()
    return render(request, 'eleves/index.html', {'eleves': eleves})

#Les détails de chaque eleve
def eleve(request, id):
    try:
        details = Eleve.objects.get(id=id)
        matieres = Matiere.objects.filter(eleve=details)
        count = matieres.count()
    except Eleve.DoesNotExist:
        raise Http404("Cet eleve n'existe pas")
    
    return render(request, 'eleves/details.html', {'details': details,'matieres':matieres,'count':count})

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