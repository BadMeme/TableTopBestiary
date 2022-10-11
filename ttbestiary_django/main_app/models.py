from django.db import models
from django.contrib.auth.models import User
import time

# Create your models here.

class ProtoChar(models.Model):
    # 
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    bio = models.TextField(max_length=500)
    #verified_artist < dont need
    created_at = models.DateTimeField(auto_now_add=True)

    #
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default =1)

    def __str__(self): 
        return self.name
    
    class Meta:
        ordering = ['created_at']

class ProtoSheet(models.Model):
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
    subclass_code = models.Charfield(max_length=3)
    #models.ForeignKey
    # stats_chart = models.Charfield(max_length=100)
    # skill_chart = models.Charfield(max_length=100)
    # spell_list_id = models.Charfield(max_length=100)
    #


class ProtoCamp(models.Model):
    name = models.Charfield(max_length=100)
    description = models.Charfield(max_length=500)

    #
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self): 
        return self.name
    
    class Meta:
        ordering = ['created_at']