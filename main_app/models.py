import code
from email.policy import default
from operator import mod
from re import I
from django.db import models
from django.contrib.auth.models import User
import time

# Create your models here.

class ProtoChar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="protochar")
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    img = models.CharField(max_length=500, default='https://mythologian.net/wp-content/uploads/2018/02/Metatrons-Cube-Symbol-Flower-Of-Life-Meaning-Symbolism-Story-1024x1024.jpg')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name
    
    class Meta:
        ordering = ['created_at']

class ProtoSheet(models.Model):
    protochar = models.OneToOneField(ProtoChar, on_delete=models.CASCADE, related_name="protosheet")
    level = models.IntegerField()
    
    RACE_CHOICES = [
        ('Human' , 'Human'), 
        ('Elf' , 'Elf'),
        ('Dwarf' , 'Dwarf'), 
        ('Halfling' , 'Halfling'),
        ('Half-Elf' , 'Half-Elf'),
        ('Half-Orc' , 'Half-Orc'),
        ('Gnome' , 'Gnome'),
        ('Dragonborn' , 'Dragonborn'),
        ('Tiefling' , 'Tiefling'),
    ]
    race = models.CharField(
        max_length=10,
        choices=RACE_CHOICES,
        default='Human'
    )

    BASE_CLASS_CHOICES = [
        ('Artificer' , 'Artificer'),
        ('Barbarian' , 'Barbarian'), 
        ('Bard' , 'Bard'), 
        ('Cleric' , 'Cleric'), 
        ('Druid' , 'Druid'), 
        ('Fighter' , 'Fighter'),
        ('Monk' , 'Monk'),
        ('Paladin' , 'Paladin'),
        ('Ranger', 'Ranger'),
        ('Rogue', 'Rogue'),
        ('Sorcerer', 'Sorcer'),
        ('Warlock', 'Warlock'),
        ('Wizard', 'Wizard'),
    ]

    base_class = models.CharField(
        max_length=10,
        choices=BASE_CLASS_CHOICES,
        default='Artificer'
    )

    # background = models.CharField()

    # level = models.IntegerField()

    str_stat = models.IntegerField()
    dex_stat = models.IntegerField()
    con_stat = models.IntegerField()
    int_stat = models.IntegerField()
    wis_stat = models.IntegerField()
    cha_stat = models.IntegerField()

    hp = models.IntegerField()
    ac = models.IntegerField()
    initiative = models.IntegerField()

    proficiency = models.IntegerField()

    str_save = models.BooleanField(default=False)
    dex_save = models.BooleanField(default=False)
    con_save = models.BooleanField(default=False)
    int_save = models.BooleanField(default=False)
    wis_save = models.BooleanField(default=False)
    cha_save = models.BooleanField(default=False)
    
    acrobatics = models.BooleanField(default=False)
    animal_handling = models.BooleanField(default=False)
    arcana = models.BooleanField(default=False)
    athletics = models.BooleanField(default=False)
    deception = models.BooleanField(default=False)
    history = models.BooleanField(default=False)
    insight = models.BooleanField(default=False)
    intimidation = models.BooleanField(default=False)
    investigation = models.BooleanField(default=False)
    medicine = models.BooleanField(default=False)
    nature = models.BooleanField(default=False)
    perception = models.BooleanField(default=False)
    performance = models.BooleanField(default=False)
    persuasion = models.BooleanField(default=False)
    religion = models.BooleanField(default=False)
    sleight_of_hand = models.BooleanField(default=False)
    survival = models.BooleanField(default=False)
    

    #models.ForeignKey
    # stats_chart = models.Charfield(max_length=100)
    # skill_chart = models.Charfield(max_length=100)
    # spell_list_id = models.Charfield(max_length=100)

class ProtoCamp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=500)
    public = models.BooleanField(default=False)
    img = models.CharField(max_length=500, default='https://cdn4.iconfinder.com/data/icons/video-game-items-concepts/128/magic-spell-book-open-512.png')
    #

    def __str__(self): 
        return self.name
    
    class Meta:
        ordering = ['name']

class MemberList(models.Model):
    campaign = models.ForeignKey(ProtoCamp, on_delete=models.CASCADE, related_name='registry')
    member = models.ForeignKey(ProtoChar, on_delete=models.CASCADE, related_name='member')

class MemberRequest(models.Model):
    character = models.OneToOneField(ProtoChar, on_delete=models.CASCADE, related_name='request')
    campaign = models.ForeignKey(ProtoCamp, on_delete=models.CASCADE, related_name='campaign')



# class Game(models.Model):
#     name = models.CharField
#     build this out to integrate multiple rulesets for character creation


# class Stats(models.Model):
#     # game = models.ForeignKey(Game, on_delete=models.Cascade, default=1)
#     protosheet = models.OneToOneField(ProtoSheet, on_delete=models.CASCADE, related_name="stats")
#     Str = models.CharField
#     Dex = models.CharField
#     Con = models.CharField
#     Int = models.CharField
#     Wis = models.CharField
#     Con = models.CharField

# class Saves(models.Model):
#     protosheet = models.OneToOneField(ProtoSheet, on_delete=models.CASCADE, related_name="saves")
#     str_save = models.BooleanField (default=False)
#     dex_save = models.BooleanField (default=False)
#     con_save = models.BooleanField (default=False)
#     int_save = models.BooleanField (default=False)
#     wis_save = models.BooleanField (default=False)
#     cha_save = models.BooleanField (default=False)

# class BaseClass(models.Model):
#     name = models.CharField
#     code = models.CharField
    
#     hd = models.CharField

#     l_arm = models.BooleanField (default=False)
#     m_arm = models.BooleanField (default=False)
#     h_arm = models.BooleanField (default=False)
#     shield = models.BooleanField (default=False)

#     str_save = models.BooleanField (default=False)
#     dex_save = models.BooleanField (default=False)
#     con_save = models.BooleanField (default=False)
#     int_save = models.BooleanField (default=False)
#     wis_save = models.BooleanField (default=False)
#     cha_save = models.BooleanField (default=False)

# class SubClass(BaseClass):
#     subclass_name = models.CharField
#     subclass_code = models.Charfield

# class RaceTemplate(models.Model):
#     name = models.CharField
#     code = models.CharField
#     # add features

# class SubRace(RaceTemplate):
#     sub_name = models.CharField
#     sub_code = models.CharField
#     # add features


# class CharSheet(models.Model) :
#     char = models.OneToOneField(Char, on_delete=models.CASCADE)
#     level = models.CharField
#     stats = models.ForeignKey(Stats)
#     race = models.ForeignKey(Race)
#     base_class = models.ForeignKey(BaseClass)
#     sub_class = models.ForeignKey(SubClass)

