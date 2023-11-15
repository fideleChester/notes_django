
from django.db.models import Avg

def calcul_moyenne_eleve_par_matiere(matieres):
    moyennes = []
    for matiere in matieres:
        moyenne = matiere.note_set.aggregate(Avg('valeur',default=0))['valeur__avg']
        moyennes.append(moyenne)
    return moyennes

def moyenne_generale_eleve(moyennes):
    moyenne = sum(moyennes) / len(moyennes)
    return moyenne
