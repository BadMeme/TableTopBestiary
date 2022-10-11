from django.shortcuts import render
from django.views import View #
from django.views.generic.base import TemplateView
from django.http import HttpResponse 
# Create your views here.

# ----- Test Models

# class TestUser : 
    
class TestChar :
    def __init__ (self, name, class_1, level=1, player=True, usercode='0'):
        
        self.name = name # pf
        self.user = usercode # fk 
        self.class_1 = class_1
        self.level = level
        self.player = player

testClasses = [
    {
        'name' : 'Fighter'
    },
    {
        'name' : 'Cleric'
    },
    {
        'name' : 'Wizard'
    },
    {
        'name' : 'Rogue'
    }
]

samples = [
    TestChar('Dave', testClasses[0]['name']),
    TestChar('Stink', testClasses[1]['name']),
    TestChar('Gandalf 2', testClasses[2]['name']),
    TestChar('Edge', testClasses[3]['name'])
]

# ----- End Test Models

class Home(View):
    def get(self, request):
        return HttpResponse('Home page. Links to: Login/Signup')

class Login(View):
    def get(self, request):
        return HttpResponse('Login Page. Creates and/or Logs in to user. Redirects to user profile')

class About(View):
    def get(self, request):
        return HttpResponse('D&D Bestiary is a companion tool for the tabletop role-playing game Dungeons & Dragons (5e). It aims to store and organize your character sheets and campaign information in one place for ease of use with integrated game tools, like dice rolling and an initiative tracker.')

# class Character(View):
#     def get(self, request):
#         return HttpResponse('Character View Page. Update button links to edit function. Delete button to remove from db. Links back to user profile and to related campaigns.')

class Character(TemplateView):
    template_name = 'test.html'

class CharacterList(TemplateView):
    template_name = 'test_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['charsheets'] = samples
        print(f"Testing: {context['charsheets'][0].name}")
        return context
        # return HttpResponse(f"{context[0].name}")
