import code
from operator import mod
from django.db import models
from django.contrib.auth.models import User
import time

# Create your models here.

class ProtoChar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name="protochar")
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    img = models.CharField(max_length=500, default='https://mythologian.net/wp-content/uploads/2018/02/Metatrons-Cube-Symbol-Flower-Of-Life-Meaning-Symbolism-Story-1024x1024.jpg')
    #verified_artist < dont need
    created_at = models.DateTimeField(auto_now_add=True)
    #

    def __str__(self): 
        return self.name
    
    class Meta:
        ordering = ['created_at']

class ProtoSheet(models.Model):
    protochar = models.OneToOneField(ProtoChar, on_delete=models.CASCADE)
    level = models.CharField(max_length=2)
    race_code = models.CharField(max_length=3) 
    class_code = models.CharField(max_length=3)
    subclass_code = models.CharField(max_length=3, default="n/a")
    #models.ForeignKey
    # stats_chart = models.Charfield(max_length=100)
    # skill_chart = models.Charfield(max_length=100)
    # spell_list_id = models.Charfield(max_length=100)
    #



class ProtoCamp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=500)
    img = models.CharField(max_length=500, default='https://cdn4.iconfinder.com/data/icons/video-game-items-concepts/128/magic-spell-book-open-512.png')
    #

    def __str__(self): 
        return self.name
    
    class Meta:
        ordering = ['name']

# class Game(models.Model):
#     name = models.CharField
#     build this out to integrate multiple rulesets for character creation


class Stats(models.Model):
    # game = models.ForeignKey(Game, on_delete=models.Cascade, default=1)
    protosheet = models.OneToOneField(ProtoSheet, on_delete=models.CASCADE, related_name="stats")
    Str = models.CharField
    Dex = models.CharField
    Con = models.CharField
    Int = models.CharField
    Wis = models.CharField
    Con = models.CharField

class Saves(models.Model):
    protosheet = models.OneToOneField(ProtoSheet, on_delete=models.CASCADE, related_name="saves")
    str_save = models.BooleanField (default=False)
    dex_save = models.BooleanField (default=False)
    con_save = models.BooleanField (default=False)
    int_save = models.BooleanField (default=False)
    wis_save = models.BooleanField (default=False)
    cha_save = models.BooleanField (default=False)

class BaseClass(models.Model):
    name = models.CharField
    code = models.CharField
    
    hd = models.CharField

    l_arm = models.BooleanField (default=False)
    m_arm = models.BooleanField (default=False)
    h_arm = models.BooleanField (default=False)
    shield = models.BooleanField (default=False)



    str_save = models.BooleanField (default=False)
    dex_save = models.BooleanField (default=False)
    con_save = models.BooleanField (default=False)
    int_save = models.BooleanField (default=False)
    wis_save = models.BooleanField (default=False)
    cha_save = models.BooleanField (default=False)

# class SubClass(BaseClass):
#     subclass_name = models.CharField
#     subclass_code = models.Charfield

class RaceTemplate(models.Model):
    name = models.CharField
    code = models.CharField
    # add features

class SubRace(RaceTemplate):
    sub_name = models.CharField
    sub_code = models.CharField
    # add features


# class CharSheet(models.Model) :
#     char = models.OneToOneField(Char, on_delete=models.CASCADE)
#     level = models.CharField
#     stats = models.ForeignKey(Stats)
#     race = models.ForeignKey(Race)
#     base_class = models.ForeignKey(BaseClass)
#     sub_class = models.ForeignKey(SubClass)

