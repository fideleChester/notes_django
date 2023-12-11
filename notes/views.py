from django.shortcuts import redirect, render,get_object_or_404,HttpResponse
from .models import Eleve,Matiere,Niveau,Note
from django.http import Http404
from .forms import NoteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required
import os
from templating_ifnti.controleur import generate_pdf

#Mes modules
from .methodes import *
# Create your views here.
def index(request):
    return render(request, 'base.html')

#La vue de tous les eleves


@login_required(login_url="/accounts/login/")
@permission_required("notes.view_eleve")
def eleves(request):
    niveaux  = Niveau.objects.all().order_by('nom')
    eleves  = Eleve.objects.all()
    return render(request, 'eleves/index.html', {'eleves': eleves,'niveaux':niveaux})
   
#Les détails de chaque eleve
@login_required(login_url="/accounts/login/")
@permission_required("notes.view_eleve")
def eleve(request, id):
    moyennes = []
    try:
        # La moyenne de cet éléve rangée dans le tableau
        
        eleve = Eleve.objects.get(id_eleve=id)
        matieres = eleve.niveau.matiere_set.all()
        
        dict_notes =[]
        list_notes = []
        table_sup = []
        
        
        for matiere in matieres:
            table_matiere = []
            table_matiere.append(matiere.nom)
            table_matiere.append(matiere.id)
            note_eleve = matiere.note_set.filter(eleve = eleve,matiere=matiere)
            for note in note_eleve:
                list_notes.append(note)
                #Tableau des matières
            table_sup.append(table_matiere)
            #liste des notes
            table_sup.append(list_notes)
            #La myenne pour chaque matiere d'un élève
            moyenne = matiere.note_set.filter(eleve = eleve).aggregate(methods_eleve.Avg('valeur',default=0))['valeur__avg']
            
            moyennes.append(moyenne)
            
            table_matiere.append(moyenne)
            
            dict_notes.append(table_sup)
            
            list_notes = []
            table_sup = []
            table_matiere = []
       
        # Calcul de la moyenne de chaque matière
        moyennne_generale = methods_eleve.moyenne_generale_eleve(moyennes)
        
        context = {
            'eleve': eleve,
            'matieres':zip(moyennes,matieres),
            "moyenne_generale":moyennne_generale,
            "matiere_notes":dict_notes
        }
        
    except Eleve.DoesNotExist:
        raise Http404("Cet eleve n'existe pas")
       
    return render(request, 'eleves/details.html',context )

#La vue des matieres
@login_required(login_url="/accounts/login/")
@permission_required("notes.view_matiere")
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



@login_required(login_url="/accounts/login/")
@permission_required("notes.add_note")
def add_note(request,eleve,matiere):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        
        #Valider les champs 
        if form.is_valid():
            
            
            note = request.POST['valeur']
            try:
                eleve = Eleve.objects.get(id_eleve=eleve)
            except Eleve.DoesNotExist:  
                raise Http404("Cet eleve n'existe pas")
            
            
            """            
            La methode pour verifier si l'élève suit la matiere, True si vrai
            """            
            
            eleve_suit_matiere = methods_eleve.verifie_eleve_suit_matiere(eleve=eleve,matiere=matiere)
            
            if not eleve_suit_matiere:
                raise Http404("Cet eleve ne suit pas cette matiere")
            else:
                sav_note = Note(valeur=note,eleve_id=eleve.id_eleve,matiere_id=matiere)
                sav_note.save()
                
            """ 
            On redirige vers les détails de l'élève
            """            
                
            return redirect('notes:eleve',id=eleve.id_eleve)            
            
    else:
        form = NoteForm()

    return render(request, 'notes/add_note.html',{'form':form})



'''RETRIEVES ALL STUDENTS '''



def listEleves(request):
    # ALL STUDENTS IN DATABASE
    queryset = Eleve.objects.all()
    # TRANSFORME OBJECTS TO DICTIONNAIRE
    lists = list(queryset.values())
    # STUDENTS DICTIONNAIRE
    dictionary_list = {
           "eleves":lists
        }
    # GENERATE PDF
    generate_pdf(dictionary_list)
    # RELATIVE PATH
    path_to_the_file = 'templating_ifnti/out/liste_eleves.pdf'
    if path_to_the_file.endswith('.pdf'):
        if os.path.exists(path_to_the_file):
            with open(path_to_the_file, 'rb') as file:
                response = HttpResponse(file.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename="liste des élèves"'
                return response
        else:
            return Http404("Le fichier PDF n'a pas été trouvé.")
    else:
        return Http404("Le fichier n'est pas au format attendu (.pdf)")

def liste_niveauElv(request,id_niveau):
    # ALL STUDENTS IN DATABASE in this level
    queryset = Eleve.objects.filter(niveau_id=id_niveau)
    # TRANSFORME OBJECTS TO DICTIONNAIRE
    lists = list(queryset.values())
    # STUDENTS DICTIONNAIRE
    dictionary_list = {
           "eleves":lists
        }
    # GENERATE PDF
    generate_pdf(dictionary_list)
    # RELATIVE PATH
    path_to_the_file = 'templating_ifnti/out/liste_eleves.pdf'
    if path_to_the_file.endswith('.pdf'):
        if os.path.exists(path_to_the_file):
            with open(path_to_the_file, 'rb') as file:
                response = HttpResponse(file.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename="liste des élèves"'
                return response
        else:
                    return Http404("Le fichier PDF n'a pas été trouvé.")
    else:
        return Http404("Le fichier n'est pas au format attendu (.pdf)")
    # ALL STUDENTS IN DATABASE
    
    
    