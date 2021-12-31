from django.db import models

# Create your models here.

from project.settings import TEMPLATES

# Create your models here.


class petitions (models.Model):
    Num_enr = models.IntegerField(default = 0 )
    date_declaration= models.DateTimeField(auto_now=False)
    #num_cit = models.IntegerField()
    cit = models.OneToOneField('citoyen', on_delete=models.CASCADE)

    object = models.TextField(max_length = 500)
    finish = models.BooleanField(default=False)
    code_req = models.CharField(max_length=250)
    dom = models.ForeignKey('domaine', on_delete=models.CASCADE)
    com = models.ForeignKey('commune', on_delete=models.CASCADE)
    agent = models.CharField(max_length=50)
    

    def __str__(self):
        return self.object

    
class  domaine (models.Model):
    num_dom = models.IntegerField()
    domaine_ar = models.CharField( max_length=150)
    domaine_fr = models.CharField(max_length=150)

    def __str__(self):
        return self.domaine_fr

class direction(models.Model):
    num_dir = models.IntegerField()
    code_dir = models.CharField(max_length=20)
    direction = models.CharField( max_length=150)
    direction_ar = models.CharField(max_length=150)
    poste_dir =  models.CharField( max_length=50)


    def __str__(self):
        return self.direction_ar

class citoyen(models.Model):
    num_cit = models.IntegerField()
    Nom = models.CharField( max_length=50)
    prenom = models.CharField( max_length=50)
    tel =  models.CharField( max_length=10)
    mail = models.EmailField( max_length=254)
    addr = models.CharField( max_length=150)

    def __str__(self):
        return self.Nom
    
class commune(models.Model):
    codseq = models.IntegerField()
    commune_ar = models.CharField( max_length=50)
    commune_fr = models.CharField( max_length=50)
    code_wil = models.IntegerField()
    def __str__(self):
        return self.commune_ar
    