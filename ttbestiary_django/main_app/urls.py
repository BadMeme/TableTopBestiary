# from ssl import VERIFY_ALLOW_PROXY_CERTS
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'), #
    path('about/', views.About.as_view(), name='about'),
    path('login/', views.Login.as_view(), name='login'),
    path('characters/', views.CharacterList.as_view(), name='test_list'),
    path('characters/<int:pk>/', views.Character.as_view(), name='test'),
    # path('profile/', views.Profile.as_view(), name='profile'),
    # path('profile/characters/', views.CharacterList.as_view(), name='char_list'),
    # path('profile/characters/new', views.CharacterCreate.as_view(), name='char_create'),
    # path('profile/characters/<int:pk>', views.Character.as_view(), name="char_detail"),
    # path('profile/characters/<int:pk>/edit', views.CharacterUpdate.as_view(), name="char_edit"),
    # path('profile/characters/<int:pk>/delete', views.CharacterDelete.as_view(), name="char_delete"),
]