# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
import time
# Create your models here.

class Ville(models.Model):
    nom = models.CharField(max_length = 100, unique = True)
    
    def __unicode__(self):
        return self.nom

class Badge(models.Model):
    description = models.CharField(max_length = 300)
    slug = models.CharField(max_length = 300)
    folder_id = int(time.time())
    image = models.FileField(upload_to='upload/badges/%s/' % (folder_id))
    
    def __unicode__(self):
        return self.slug

class Profile(models.Model):
    user = models.ForeignKey(User , unique = True)
    folder_id = int(time.time())
    image = models.FileField(upload_to='upload/avatars/%s/' % (folder_id) , blank = True)
    # Interests
    apropos = models.TextField()
    siteweb = models.CharField(max_length = 100)
    facebook = models.CharField(max_length = 100, unique = True)
    referral_code = models.CharField(max_length = 10)
    credit = models.IntegerField(default = 0)
    badges = models.ManyToManyField(Badge, blank = True)
    friends = models.ManyToManyField('self')
    GENDER_CHOICES = (
        ('H', 'Homme'),
        ('F', 'Femme')
    )
    sexe = models.CharField(max_length = 1, choices = GENDER_CHOICES)
    ville = models.CharField(max_length = 100)
    
    def __unicode__(self):
        return "%s %s" % (self.prenom, self.nom)
        
class Message(models.Model):
    titre = models.CharField(max_length = 300)
    text = models.TextField()
    de_utilisateur = models.ForeignKey(User, related_name = "message_de_utilisateur")
    a_utilisateur = models.ForeignKey(User, related_name = "message_a_utilisateur")
    de_supprime = models.BooleanField(default = False)
    a_supprime = models.BooleanField(default = False)
    date = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return self.titre
    
class Reponse(models.Model):
    message = models.ForeignKey(Message)
    text = models.TextField()
    de_utilisateur = models.ForeignKey(User)
    token = models.CharField(max_length = 100, unique = True)
    
    def __unicode__(self):
        return self.text
    
class Restaurant(models.Model):
    nom = models.CharField(max_length = 100)
    ville = models.ForeignKey(Ville)
    adresse = models.CharField(max_length = 300)
    tel = models.CharField(max_length = 30, blank = True)
    
    def __unicode__(self):
        return self.nom
    
class Repas(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    prix = models.IntegerField()
    date = models.DateTimeField()
    places = models.IntegerField()
    folder_id = int(time.time())
    image = models.FileField(upload_to='upload/meals/%s/' % (folder_id))
    
class Menu(models.Model):
    repas = models.ForeignKey(Repas)
    titre = models.CharField(max_length = 300)
    description = models.CharField(max_length = 300, blank = True)
    TYPE_CHOICES = (
        ("entrees","Entrées"),
        ("plats", "Plats"),
        ("desserts","Desserts")
    )
    categorie = models.CharField(max_length = 15, choices = TYPE_CHOICES)
    
class Reservation(models.Model):
    utilisateur = models.ForeignKey(User)
    repas = models.ForeignKey(Repas)
    date = models.DateTimeField(auto_now_add = True)
    transaction = models.CharField(max_length = 100)
    
class Fact(models.Model):
    text = models.TextField()
    de_utilisateur = models.ForeignKey(User, related_name = "fact_de_utilisateur")
    a_utilisateur = models.ForeignKey(User, related_name = "fact_a_utilisateur")
    date = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return self.text
     
class Referral(models.Model):
    referrer = models.ForeignKey(User, related_name = "utilisateur_invit")
    referred = models.ForeignKey(User, related_name = "utilisateur_invite_par")
    date = models.DateTimeField(auto_now_add = True)
    
    class meta:
        unique_together = (("referrer", "referred"),)


