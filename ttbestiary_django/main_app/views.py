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
#
from formtools.wizard.views import SessionWizardView

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

class CharacterSheet(TemplateView):
    template_name = 'render_char.html'
    test_context = {
        'info' : {
            'name' : 'Test Character',
            'level' : 1,
            'pro' : 2
        },
        'race' : {
            'name' : 'Test Race',
        },
        'class' : {
            'classname' : 'Test Class',
            'hd' : 10
        },
        'stats' : {
            'str' : 15,
            'dex' : 14,
            'con' : 13,
            'int' : 10,
            'wis' : 12,
            'cha' : 8
        },
        'stats_2' : {
            'HP' : 11,
            'AC' : 15,
            'Initiative' : 2
        },
        'saves' : {
            'str' : True,
            'dex' : False,
            'con' : True,
            'int' : False,
            'wis' : False,
            'cha' : False
        },
        'skills' : {
            'test_skill_1' : False,
            'test_skill_2' : False,
            'test_skill_3' : True,
            'test_skill_4' : False,
            'test_skill_5' : True,
            'test_skill_6' : False,
        }
    }
    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        #
        #
        #
        context = self.test_context
        print(context['class']['classname'])
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

#### Form Wizard Shit ###

# Create Character 
# 1) Name, Bio, Level, misc details
# 2) Choose Race, # refactor => make Race-dependent choices
# 3) Choose Class # refactor => make class-dependent choice
# 4) Assign Stats # refactor => Choose method: Manual, Std_arr, point buy, Roll
# # 5) Starting Equiptment/Gold
# # 6) Make choices for level - dependent features. Repeat process for every level of created character
# # 7) Calculate secondary stats
# # 8) Finalize Character sheet

class CharGenForm1(forms.Form):
    name = forms.CharField()
    bio = forms.CharField()
    level = forms.IntegerField(initial=1)

step_2_choices = [
    ('hum', 'Human'), ('elf', 'Elf'), ('dwa', 'Dwarf'), ('hal', 'Halfling')
    ]
class CharGenForm2(forms.Form):
    race = forms.MultipleChoiceField(
        required=False,
        choices = step_2_choices
    )
    #note racial modifiers that need to be stored (bonus proficiencies, stat modifiers, etc)
    #if there are race based options, liks starting spells, etc, generate a list and allow one to be selected
    temp_option_r_1 = forms.CheckboxInput()
    temp_option_r_2 = forms.CheckboxInput()

step_3_choices = [
    ('fig', 'Fighter'), ('wiz', 'Wizard'), ('cle', 'Cleric'), ('rog', 'Rogue')
    ]
class CharGenForm3(forms.Form):
    base_class = forms.MultipleChoiceField(
        required=False,
        choices = step_3_choices
    )
    #find list of class skills, allow user to select specified number from list and save those inputs
    temp_skills = forms.CheckboxSelectMultiple()
    # if there are class based options at level 1, generate a list and allow one to be selected
    temp_option_c_1 = forms.CheckboxInput()
    temp_option_r_2 = forms.CheckboxInput()
    # note and store relevant template info: HD, proficiencies, etc.

class CharGenForm4(forms.Form):
    #based on rules => iterate through a list of stats and generate an input field for each
    #for now, manual input and D&D5e rules assumed, but in the future can add options for STD array and rolling
    str = forms.IntegerField(initial=10)
    dex = forms.IntegerField(initial=10)
    con = forms.IntegerField(initial=10)
    int = forms.IntegerField(initial=10)
    wis = forms.IntegerField(initial=10)
    cha = forms.IntegerField(initial=10)

    #make sure to indicate stat bonuses from race
step_5_choices = [
    ('a', 'Gold'), ('b', 'Preset A'), ('c', 'Preset B')
    ]

class CharGenForm5(forms.Form):
    
    #note the options provided by base class and render them here from state
    equip_option_1 = forms.MultipleChoiceField(
        required = False,
        choices = step_5_choices
    )

step_6_choices = [
    ('a', 'skill_a'), ('b', 'skill_b'), ('c', 'skill_c'), ('d', 'skill_d')
    ]

class CharGenForm6(forms.Form):
    #If there is a class dependant option at your level, answer prompt here
    #Loop through this step for every level dependent class feature
    level_opt_c = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices = step_6_choices
    )

step_6_choices = [
    ('a', 'skill_a'), ('b', 'skill_b'), ('c', 'skill_c'), ('d', 'skill_d')
    ]

class CharGenForm7(forms.Form):
    #if level > 1 and there is a race dependent option at your level, answer prompt here
    #Loop Through This step for evey level dependent race feature
    level_opt_r = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices = step_6_choices
    )

class CharGenFormFinalize(forms.Form):
    # review the current state of the character's input fields and finalize. On submission, 
    # Secondary stats will be calculated and saved, and all forms will write their respective objects to the DB, linked to the created Character
    def get_context_data(self, **kwargs):
        context = 'placeholder'
        return context
    
# WIZARD TIME
class ContactForm1(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()
class ContactForm2(forms.Form):
    message = forms.CharField(widget=forms.Textarea)

class CharGenWizard(SessionWizardView):
    form_list = [CharGenForm1, CharGenForm2, CharGenForm3, CharGenForm4, CharGenForm5, CharGenForm6, CharGenForm7]
    def get_template_names(self):
        return 'form_wizard.html'
    def done(self, form_list, form_dict, **kwargs):
        # return render(self.request, 'done.html', {
        #     'form_data': [form.cleaned_data for form in form_list],
        # })
        return render(self.request, 'home.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })