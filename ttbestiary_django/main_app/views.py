# from socketserver import _RequestType
# from xml.sax.handler import property_declaration_handler

from django import forms
from django.shortcuts import render
from django.forms import ModelForm
from django.views import View #
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse 

#models
from .models import ProtoChar, ProtoSheet, ProtoCamp

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


# ----- End Test Models

# ----- Forms


class SheetInput(forms.Form):
    #fields = ['level', 'race_code', 'class_code', 'subclass_code']
    level = forms.NumberInput
    race_code = forms.MultipleChoiceField
    class_code = forms.MultipleChoiceField
    subcloass_code = forms.MultipleChoiceField

class SheetForm(ModelForm):
    class Meta:
        model = ProtoSheet
        fields = ['protochar', 'level', 'race_code', 'class_code', 'subclass_code']
    
        # def __init__(self, *args, **kwargs):
        #     super(SheetForm, self).__init__(*args, **kwargs)
        #     self.fields['protochar'].disabled = True
        # exclude = ['protochar']
        # level = forms.CharField (label='level', max_length=2)
        # race_code = forms.CharField (label='race_code', max_length=3)
        # class_code = forms.CharField (label='class_code', max_length=3)
        # subclass_code = forms.CharField (label='subclass_code', max_length=3)
        # # !need place for foreign key probably 


# -----

class Home(TemplateView):
    template_name = 'home.html'

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/signup.html', context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile') #this doesnt seem to work
        else:
            context = {'form': form}
            return render(request, 'registration/signup.html', context)

class Sheet(View):
    def get(self, request, *args, **kwargs):
        form = SheetForm(initial={'protochar': kwargs['pk']})
        form.fields['protochar'].disabled = True
        context = {'form': form}
        return render(request, 'sheet/sheet_gen.html', context)

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.POST['protochar'] = kwargs['pk']
        form = SheetForm(request.POST)
        if form.is_valid():
            sheet = form.save()
            print(sheet)
            return redirect('char/char_sheet', kwargs['pk'])
        else:
            context = {'form': form}
            return render(request, 'sheet/sheet_gen.html', context)

class About(View):
    def get(self, request):
        return HttpResponse('D&D Bestiary is a companion tool for the tabletop role-playing game Dungeons & Dragons (5e). It aims to store and organize your character sheets and campaign information in one place for ease of use with integrated game tools, like dice rolling and an initiative tracker.')

class Profile(TemplateView):
    template_name = 'profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # if self.request.user == False :
        #     return redirect('home')
        # context['test'] = self.request.user.protochar.all()
        context['chars'] = ProtoChar.objects.all().filter(user = self.request.user.pk)
        context['camps'] = ProtoCamp.objects.all().filter(user = self.request.user.pk)
        # print(context['test'])
        return context

class CharDetail(DetailView):
    model = ProtoChar
    template_name="char/char_sheet.html"
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(context)
    
class CampDetail(DetailView):
    model = ProtoCamp
    template_name="camp/camp_detail.html"

# class Sheet(DetailView):
#     model = ProtoSheet
#     template_name = 'sheet_view.html'

# character CRUD routes
class CharCreate(CreateView):
    model = ProtoChar 
    fields = ['name', 'img', 'bio']
    template_name = 'char/char_gen.html'
    success_url = '/profile/'

class CharUpdate(UpdateView):
    model = ProtoChar
    fields = ['name', 'img', 'bio']
    template_name = 'char/char_edit.html'
    success_url = '/profile/'

class CharDelete(DeleteView):
    model = ProtoChar
    template_name = 'char/char_delete.html'
    success_url = "/profile/"


# character sheet CRUD routes
# class SheetCreate(CreateView):
#     model = ProtoSheet
#     fields = ['level', 'race_code', 'class_code']
#     template_name = 'sheet_gen.html'
#     success_url = '/profile/'
#     # will need to fix. complex series of read/write calls etc.

class SheetUpdate(UpdateView):
    model = ProtoSheet
    fields = ['name', 'img', 'bio']
    template_name = 'sheet/sheet_edit.html'
    success_url = '/profile/'

class SheetDelete(DeleteView):
    model = ProtoSheet
    template_name = 'sheet/sheet_delete.html'
    success_url = "/profile/"


# campaign CRUD routes
class CampCreate(CreateView):
    model = ProtoCamp 
    fields = ['name', 'info', 'img']
    template_name = 'camp/camp_gen.html'
    success_url = '/profile/'

class CampUpdate(UpdateView):
    model = ProtoCamp 
    fields = ['name', 'info', 'img']
    template_name = 'camp/camp_edit.html'
    success_url = '/profile/'

class CampDelete(DeleteView):
    model = ProtoCamp
    template_name = 'camp/camp_delete.html'
    success_url = "/profile/"