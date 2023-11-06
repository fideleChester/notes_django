from django.shortcuts import render
from django.http import HttpResponse
from .models import Eleve,Matiere

# Create your views here.
def index(request):
    return render(request, 'notes/index.html')

#La vue de tous les eleves
from .models import Eleve,Matiere
def eleves(request):
    eleves  = Eleve.objects.all()
    return HttpResponse(eleves)

#Les détails de chaque eleve
def eleve(request, id):
    return HttpResponse("Les détails de l'eleve " + str(id))

#La vue des matieres
def matieres(request):
    matieres = Matiere.objects.all()
    return HttpResponse(matieres)

#details d'une matiere
def matiere(request, id):   
    return HttpResponse("Les détails de la matière " + str(id))

#les détails de chaque niveau
def niveau(request, id):
    return HttpResponse("Les détails du niveau " + str(id))