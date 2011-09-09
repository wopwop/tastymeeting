# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
import time
from tastymeeting.thumbs import ImageWithThumbsField
from django.forms.models import ModelForm

# Create your models here.

class Ville(models.Model):
    nom = models.CharField(max_length = 100, unique = True)
    
    def __unicode__(self):
        return self.nom

class Badge(models.Model):
    description = models.CharField(max_length = 300)
    slug = models.CharField(max_length = 300)
    folder_id = int(time.time())
    image = models.ImageField(upload_to='upload/badges/')
    
    def __unicode__(self):
        return self.slug

class Profile(models.Model):
    user = models.ForeignKey(User , unique = True)
    folder_id = int(time.time())
    image = ImageWithThumbsField(upload_to='upload/avatars/', sizes=((32,32),(52,52),(135,160),(200,220), (400,400)), null=True, blank = True)
    # Interests
    apropos = models.TextField(null=True, blank = True)
    siteweb = models.CharField(max_length = 100, null=True, blank = True)
    facebook = models.CharField(max_length = 100, null=True, blank = True)
    twitter = models.CharField(max_length=100, null=True, blank = True)
    tags = models.TextField(null=True, blank = True)
    referral_code = models.CharField(max_length = 10, null=True, blank = True)
    credit = models.IntegerField(default = 0, null=True, blank = True)
    badges = models.ManyToManyField(Badge, null=True, blank = True)
    friends = models.ManyToManyField('self', null=True, blank = True)
    GENDER_CHOICES = (
        ('H', 'Homme'),
        ('F', 'Femme')
    )
    sexe = models.CharField(max_length = 1, choices = GENDER_CHOICES, null=True, blank = True)
    ville = models.CharField(max_length = 100, null=True, blank = True)
    birthdate = models.DateField(null=True, blank = True)
        
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
    lieu = models.CharField(max_length = 300)
    adresse = models.CharField(max_length = 500)
    tel = models.CharField(max_length = 30, blank = True)
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.nom
    
class Repas(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    prix = models.IntegerField()
    date = models.DateTimeField()
    places = models.IntegerField()
    folder_id = int(time.time())
    image = ImageWithThumbsField(upload_to='upload/meals/', sizes=((110,75),(460,350),(230,140)))
    
    def __unicode__(self):
        return self.restaurant.nom
    
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


