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
    # stats = {
    #     'str' : models.CharField(max_length=2), 
    #     'dex' : models.CharField(max_length=2), 
    #     'con' : models.CharField(max_length=2), 
    #     'int' : models.CharField(max_length=2), 
    #     'wis' : models.CharField(max_length=2), 
    #     'cha' : models.CharField(max_length=2), 
    # }
    #these will be possibly be models.ForeignKeys
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