
from django.db.models import Avg
import os
from django.shortcuts import get_object_or_404,HttpResponse,Http404

def calcul_moyenne_eleve_par_matiere(matieres):
    moyennes = []
    for matiere in matieres:
        moyenne = matiere.note_set.aggregate(Avg('valeur',default=0))['valeur__avg']
        moyennes.append(moyenne)
    return moyennes

def moyenne_generale_eleve(moyennes):
    moyenne = 0
    try:
        moyenne = sum(moyennes) / len(moyennes)
    except:
        pass
    return moyenne


def verifie_eleve_suit_matiere(eleve, matiere):
    """
    Renvoie True si l'élève suit la matière, False sinon
    """
    return eleve.niveau.matiere_set.filter(pk=matiere).exists()


# def view_pdf(path_to_the_file):
#     if path_to_the_file.endswith('.pdf'):
#         if os.path.exists(path_to_the_file):
#             with open(path_to_the_file, 'rb') as file:
#                 response = HttpResponse(file.read(), content_type='application/pdf')
#                 response['Content-Disposition'] = 'inline; filename="liste des élèves"'
#                 return response
#         else:
#             return Http404("Le fichier PDF n'a pas été trouvé.")
#     else:
#         return Http404("Le fichier n'est pas au format attendu (.pdf)")