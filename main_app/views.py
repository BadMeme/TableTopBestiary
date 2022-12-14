# from socketserver import _RequestType
# from xml.sax.handler import property_declaration_handler

from pyexpat import model
from django import forms
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.forms import ModelForm
from django.views import View #
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse 
#
from formtools.wizard.views import SessionWizardView

#models
from .models import ProtoChar, ProtoSheet, ProtoCamp, MemberList, MemberRequest

#login/register
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
#auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#@method_decorator(login_required, name='dispatch')

# -----

# ----- Forms

class CharForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CharForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True
    
    class Meta:
        model = ProtoChar
        fields = '__all__'

class SheetForm(ModelForm):
    
    class Meta:
        model = ProtoSheet
        fields = '__all__'

class CampForm(ModelForm):
    
    class Meta:
        model = ProtoCamp
        fields = '__all__'

class MemberListForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MemberListForm, self).__init__(*args, **kwargs)
        # self.fields['member'].disabled = True

    class Meta:
        model = MemberList
        fields = '__all__'

class MemberRequestForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(RequestForm, self).__init__(*args, **kwargs)
    #     self.fields['__all__'].disabled = True

    class Meta:
        model = MemberRequest
        fields = '__all__'

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
            return redirect('profile') 
        else:
            context = {'form': form}
            return render(request, 'registration/signup.html', context)


class About(View):
    def get(self, request):
        return HttpResponse('D&D Bestiary is a companion tool for the tabletop role-playing games. The coure functionality aims to automate and validate against complex TTRP rulesets and put players in touch with other players looking for games. Currently supporting the core rules of Dungeons & Dragons (5e). ttBestiary builds, validates, stores, and organizes your character sheets and campaign information in one place for ease of use with integrated game tools, like dice rolling and an initiative tracker.')

@method_decorator(login_required, name='dispatch')
class Profile(TemplateView):
    template_name = 'profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chars'] = ProtoChar.objects.all().filter(user = self.request.user.pk)
        context['camps'] = ProtoCamp.objects.all().filter(user = self.request.user.pk)
        
        return context

@method_decorator(login_required, name='dispatch')
class CharDetail(DetailView):
    model = ProtoChar
    template_name="char/char_sheet.html"

@method_decorator(login_required, name='dispatch')
class CampDetail(DetailView):
    model = ProtoCamp
    template_name="camp/camp_detail.html"

@method_decorator(login_required, name='dispatch')
class CampDetailTest(TemplateView):
    
    template_name="camp/camp_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # if self.request.user == False :
        #     return redirect('home')
        # context['test'] = self.request.user.protochar.all()
        context['camp'] = ProtoCamp.objects.all().filter(id = kwargs['pk'])
        context['members'] = MemberList.objects.all().filter(campaign = kwargs['pk'])
        print(context)
        return context

@method_decorator(login_required, name='dispatch')
class SheetDetail(DetailView):
    model = ProtoSheet
    template_name = 'sheet/sheet_view.html'

# character CRUD routes
@method_decorator(login_required, name='dispatch')
class CharCreate(CreateView):
    model = ProtoChar 
    form_class = CharForm
    def get_initial(self):
        user = self.request.user.id
        return { 'user' : user }
    template_name = 'char/char_gen.html'
    success_url = '/profile/'
    #figure out how to disable the user form field

@method_decorator(login_required, name='dispatch')
class CharUpdate(UpdateView):
    model = ProtoChar
    fields = ['name', 'img', 'bio']
    template_name = 'char/char_edit.html'
    success_url = '/profile/'

@method_decorator(login_required, name='dispatch')
class CharDelete(DeleteView):
    model = ProtoChar
    template_name = 'char/char_delete.html'
    success_url = '/profile/'


# character sheet CRUD routes
@method_decorator(login_required, name='dispatch')
class SheetCreate(View):
    def get(self, request, *args, **kwargs):
        form = SheetForm(initial={
            'protochar': kwargs['pk'],
            'level' : 1,
            'str_stat': 10,
            'dex_stat': 10,
            'con_stat': 10,
            'int_stat': 10,
            'wis_stat': 10,
            'cha_stat': 10,
            'hp' : 10,
            'ac' : 10,
            'initiative' : 0,
            'proficiency' : 2,
            })
        form.fields['protochar'].disabled = True
        context = {'form': form}
        return render(request, 'sheet/sheet_gen.html', context)

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.POST['protochar'] = kwargs['pk']
        form = SheetForm(request.POST)
        if form.is_valid():
            sheet = form.save()
            return redirect('char_sheet', kwargs['pk'])
        else:
            context = {'form': form}
            return render(request, 'sheet/sheet_gen.html', context)

@method_decorator(login_required, name='dispatch')
class SheetUpdate(UpdateView):
    model = ProtoSheet
    fields = '__all__'
    template_name = 'sheet/sheet_edit.html'
    success_url = '/profile/'

@method_decorator(login_required, name='dispatch')
class SheetDelete(DeleteView):
    model = ProtoSheet
    template_name = 'sheet/sheet_delete.html'
    success_url = '/profile/'


# campaign CRUD routes
@method_decorator(login_required, name='dispatch')
class CampCreate(CreateView):
    model = ProtoCamp 
    form_class = CampForm
    def get_initial(self):
        user = self.request.user.id
        return { 'user' : user }
    template_name = 'camp/camp_gen.html'
    success_url = '/profile/'

@method_decorator(login_required, name='dispatch')
class CampUpdate(UpdateView):
    model = ProtoCamp 
    fields = ['name', 'info', 'img']
    template_name = 'camp/camp_edit.html'
    success_url = '/profile/'

@method_decorator(login_required, name='dispatch')
class CampDelete(DeleteView):
    model = ProtoCamp
    template_name = 'camp/camp_delete.html'
    success_url = "/profile/"


###

@method_decorator(login_required, name='dispatch')
class GameSearch(TemplateView):
    template_name = 'char/game_search.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['games'] = ProtoCamp.objects.all()
        
        return context

@method_decorator(login_required, name='dispatch')
class MemberRequest(TemplateView):
    template_name = 'char/request_create.html'

    def get(self, request, *args, **kwargs):
        form = MemberRequestForm(initial={
            'character' : kwargs['pk'],
            'campaign' : kwargs['camp_pk'],
            })
        # form.fields['character'].disabled = True
        context = {'form': form}
        return render(request, 'char/request_create.html', context)

    def post(self, request, *args, **kwargs):
        form = MemberRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('char_sheet', kwargs['pk'])
        else:
            context = {'form': form}
            return render(request, 'char/request_create.html', context)

@method_decorator(login_required, name='dispatch')
class MemberSearch(TemplateView):
    template_name = 'camp/member_search.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['characters'] = ProtoChar.objects.all().filter()
        
        return context

@method_decorator(login_required, name='dispatch')
class MemberRegister(TemplateView):
    template_name = 'camp/member_register.html'
    
    def get(self, request, *args, **kwargs):
        form = MemberListForm(initial={
            'campaign' : kwargs['pk'],
            'member' : kwargs['char_pk'],
            })
        # form.fields['campaign'].disabled = True
        context = {'form': form}
        return render(request, 'camp/member_register.html', context)

    def post(self, request, *args, **kwargs):
        # request.POST._mutable = True
        # request.POST['campaign'] = kwargs['pk']
        # request.POST['member'] = kwargs['char_pk']
        form = MemberListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('camp_detail', kwargs['pk']) 
        else:
            context = {'form': form}
            return render(request, 'camp/member_register.html', context)

#### Future Refactoring Ahead









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
    ('Human', 'Human'), ('Elf', 'Elf'), ('Dwarf', 'Dwarf'), ('Halfling', 'Halfling')
    ]
class CharGenForm2(forms.Form):
    race = forms.MultipleChoiceField(
        required=True,
        choices = step_2_choices
    )
    #note racial modifiers that need to be stored (bonus proficiencies, stat modifiers, etc)
    #if there are race based options, liks starting spells, etc, generate a list and allow one to be selected
    # temp_option_r_1 = forms.CheckboxInput()
    # temp_option_r_2 = forms.CheckboxInput()

step_3_choices = [
    ({'name' : 'Fighter', 'class_code': 'fig'}, 'Fighter'), ({'name' : 'Wizard', 'class_code': 'wiz'}, 'Wizard'), ({'name' : 'Cleric', 'class_code': 'cle'}, 'Cleric'), ({'name' : 'Rogue', 'class_code': 'rog'}, 'Rogue')
    ]
class CharGenForm3(forms.Form):
    base_class = forms.MultipleChoiceField(
        required=True,
        choices = step_3_choices
    )
    #find list of class skills, allow user to select specified number from list and save those inputs
    # temp_skills = forms.CheckboxSelectMultiple()
    # # if there are class based options at level 1, generate a list and allow one to be selected
    # temp_option_c_1 = forms.CheckboxInput()
    # temp_option_r_2 = forms.CheckboxInput()
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
    (True, 'skill_a'), (True, 'skill_b'), (True, 'skill_c'), (True, 'skill_d')
    ]

class CharGenForm6(forms.Form):
    #If there is a class dependant option at your level, answer prompt here
    #Loop through this step for every level dependent class feature
    level_opt_c = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices = step_6_choices
    )

step_7_choices = [
    (True, 'skill_e'), (True, 'skill_f'), (True, 'skill_g'), (True, 'skill_h')
    ]

class CharGenForm7(forms.Form):
    #if level > 1 and there is a race dependent option at your level, answer prompt here
    #Loop Through This step for evey level dependent race feature
    level_opt_r = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices = step_7_choices
    )

class CharGenFormFinalize(forms.Form):
    # review the current state of the character's input fields and finalize. On submission, 
    # Secondary stats will be calculated and saved, and all forms will write their respective objects to the DB, linked to the created Character
    def get_context_data(self, **kwargs):
        context = 'placeholder'
        return context
    
# WIZARD TIME

class CharGenWizard(SessionWizardView):
    form_list = [CharGenForm1, CharGenForm2, CharGenForm3, CharGenForm4, CharGenForm6, CharGenForm7]
    def get_template_names(self):
        return 'form_wizard.html'

    # def get_form_step_data(self, form):
    #     print(f'Test form_step_data: {form.data}')

    # def process_step(self, form):
    #     # self.get_form_step_data(form)
    #     print(f"'test': {self.steps.current}")

    def render_revalidation_failure(self, step, form, **kwargs):
        self.storage.current_step = step
        print(f'Test: {self}')
        return self.render(form, **kwargs)

    def done(self, form_list, form_dict, **kwargs):
        # for dict in form_dict:
        for form in form_dict :
            print(f"Test: done, {form}")
        return render(self.request, 'home.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })