from django.db import models

# Create your models here.
#Le modele personne
class Personne(models.Model):
    #Ses attributs
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=100,choices=(('M','Masculin'),('F','Feminin')))
    
    class Meta:
        abstract = True
    
    #le modèle elève

    
class Enseignant(Personne):
    #Ses attributs
    def __str__(self) -> str:
        return self.nom + " " + self.prenom


class Matiere(models.Model):
    nom = models.CharField(unique=True,max_length=50)
    enseignant = models.ForeignKey(Enseignant,on_delete=models.CASCADE)
    niveaus = models.ManyToManyField('Niveau')
    
    
    class Meta:
        verbose_name_plural = "Matières"
    
    def __str__(self) -> str:
        return self.nom
     

    
class Niveau(models.Model):
    nom = models.CharField(unique=True,max_length=2)
    
    class Meta:
        verbose_name_plural = "Niveaux"
    
    
    def __str__(self) -> str:
        return self.nom 
    
 
 
class Eleve(Personne):
    #Ses attributs
    id = models.IntegerField(primary_key=True)
    niveau = models.ForeignKey(Niveau,on_delete=models.CASCADE)
    # matieres = models.ManyToManyField(Matiere)
    
    class Meta:
        verbose_name_plural = "Elèves"
    
    def __str__(self) -> str:
        return "{0} {1}".format(self.nom,self.prenom)
    

class Note(models.Model):
    #ses attribut
    valeur = models.FloatField(null=True)
    #un elève a plusieurs notes
    eleve = models.ForeignKey(Eleve,on_delete=models.CASCADE) 
    matiere = models.ForeignKey(Matiere,on_delete=models.CASCADE)   
    
    def __str__(self) -> str:
        return str(self.valeur)
    
