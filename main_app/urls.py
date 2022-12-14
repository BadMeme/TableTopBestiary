# from ssl import VERIFY_ALLOW_PROXY_CERTS
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'), #
    path('about/', views.About.as_view(), name='about'),
    path('profile/', views.Profile.as_view(), name='profile'),
    #
    path('profile/character/new', views.CharCreate.as_view(), name='char_gen'),
    # Form Wizard Test
    path('profile/character/new/test', views.CharGenWizard.as_view(), name='form_wizard.html'),
    # -----
    path('profile/character/<int:pk>', views.CharDetail.as_view(), name='char_sheet'),
    path('profile/character/<int:pk>/edit', views.CharUpdate.as_view(), name="char_edit"),
    path('profile/character/<int:pk>/delete', views.CharDelete.as_view(), name="char_delete"),
    path('profile/character/<int:pk>/join', views.GameSearch.as_view(), name='game_search'),
    path('profile/character/<int:pk>/join/<int:camp_pk>', views.MemberRequest.as_view(), name='request_create'),
    #
    path('profile/character/<int:pk>/sheet/new', views.SheetCreate.as_view(), name='sheet_gen'),
    path('profile/sheet/<pk>', views.SheetDetail.as_view(), name='sheet_view'),
    path('profile/sheet/<pk>/edit', views.SheetUpdate.as_view(), name='sheet_edit'),
    path('profile/sheet/<pk>/delete', views.SheetDelete.as_view(), name='sheet_delete'),
    #
    path('profile/campaign/new', views.CampCreate.as_view(), name='camp_gen'),
    path('profile/campaign/<int:pk>/', views.CampDetail.as_view(), name="camp_detail"),
    # path('profile/campaign/<int:pk>/test', views.CampDetailTest.as_view(), name="camp_detail"),
    path('profile/campaign/<int:pk>/edit', views.CampUpdate.as_view(), name="camp_edit"),
    path('profile/campaign/<int:pk>/delete', views.CampDelete.as_view(), name="camp_delete"),
    path('profile/campaign/<int:pk>/search', views.MemberSearch.as_view(), name='member_search'),
    path('profile/campaign/<int:pk>/search/<int:char_pk>', views.MemberRegister.as_view(), name='member_register'),
    #

    path('accounts/signup/', views.Signup.as_view(), name='signup'),
    # path('accounts/logout/', views.Logout.as_view(), name='logout')

]