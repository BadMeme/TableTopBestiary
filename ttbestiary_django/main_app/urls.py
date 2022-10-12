# from ssl import VERIFY_ALLOW_PROXY_CERTS
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'), #
    path('about/', views.About.as_view(), name='about'),
    # path('login/', views.Login.as_view(), name='login'),
    path('characters/', views.CharacterList.as_view(), name='test_list'),
    path('characters/<int:pk>/', views.Character.as_view(), name='test'),
    path('profile/', views.Profile.as_view(), name='profile'),
    # path('profile/character/new', views.CharCreate.as_view(), name='char_create'),
    # path('profile/character/<int:pk>', views.Char.as_view(), name="char_detail"),
    # path('profile/character/<int:pk>/edit', views.CharUpdate.as_view(), name="char_edit"),
    # path('profile/character/<int:pk>/delete', views.CharDelete.as_view(), name="char_delete"),
    # path('profile/campaign/new', views.CharCreate.as_view(), name='camp_create'),
    # path('profile/campaign/<int:pk>', views.Camp.as_view(), name="camp_detail"),
    # path('profile/campaign/<int:pk>/edit', views.CampUpdate.as_view(), name="camp_edit"),
    # path('profile/campaign/<int:pk>/delete', views.CampDelete.as_view(), name="camp_delete"),
    path('accounts/signup/', views.Signup.as_view(), name='signup'),

]