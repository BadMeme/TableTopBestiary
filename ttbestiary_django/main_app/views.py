from django.shortcuts import render
from django.views import View #
from django.views.generic.base import TemplateView
from django.http import HttpResponse 

#login/register
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
#auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#@method_decorator(login_required, name='dispatch')
#---

# Create your views here.

# ----- Test Models

# class TestUser : 

std_arr = {
    'str' : 15,
    'dex' : 14,
    'con' : 13,
    'int' : 12,
    'wis' : 10,
    'cha' : 8
}
    
class TestChar :
    def __init__ (self, name, class_1, stats=std_arr, level=1, player=True, usercode='0'):
        
        self.name = name 
        self.user = usercode 
        self.class_1 = class_1['name']
        self.class_code = class_1['code']
        self.level = level
        self.player = player
        self.stats = stats
        self.hd = class_1['hd']
        self.saves = class_1['saves']

testClasses = [
    {
        'name' : 'Fighter',
        'code' : 'FIG',
        'hd' : 10,
        'saves' : {
            'str' : True,
            'dex' : False,
            'con' : True,
            'int' : False,
            'wis' : False,
            'cha' : False
        },
    },
    {
        'name' : 'Cleric',
        'code' : 'CLE',
        'hd' : 8,
        'saves' : {
            'str' : False,
            'dex' : False,
            'con' : False,
            'int' : False,
            'wis' : True,
            'cha' : True
        },
    },
    {
        'name' : 'Wizard',
        'code' : 'WIZ',
        'hd' : 6,
        'saves' : {
            'str' : False,
            'dex' : False,
            'con' : False,
            'int' : True,
            'wis' : True,
            'cha' : False
        },
    },
    {
        'name' : 'Rogue',
        'code' : 'ROG',
        'hd' : 8,
        'saves' : {
            'str' : False,
            'dex' : True,
            'con' : False,
            'int' : True,
            'wis' : False,
            'cha' : False
        },
    }
]

samples = [
    TestChar('Dave', testClasses[0]),
    TestChar('Stink', testClasses[1]),
    TestChar('Gandalf 2', testClasses[2]),
    TestChar('Edge', testClasses[3])
]

# ----- End Test Models

class Home(View):
    def get(self, request):
        return HttpResponse('Home page. Links to: Login/Signup')

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/signup.html', context)
    
    def post(self, request):
        form = UserCreationForm(request.Post)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            context = {'form': form}
            return render(request, 'registration/signup.html', context)

# class Login(View):
#     def get(self, request):
#         return HttpResponse('Login Page. Creates and/or Logs in to user. Redirects to user profile')

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

