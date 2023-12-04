
from django.db.models import Avg

def calcul_moyenne_eleve_par_matiere(matieres):
    moyennes = []
    for matiere in matieres:
        moyenne = matiere.note_set.aggregate(Avg('valeur',default=0))['valeur__avg']
        moyennes.append(moyenne)
    return moyennes

def moyenne_generale_eleve(moyennes):
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