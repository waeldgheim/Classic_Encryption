from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('affine/', views.affine_algo, name='affine'),
    path('affine/crack/', views.crack_affine, name='crack_affine'),
    path('affine/top_brute_force/', views.top_brute_force_affine, name='top_brute_force_affine'),
    path('vigenere/', views.vignere_cipher, name='vigenere'),
    path('monoalphabetic/', views.monoalphabetic_cipher, name='monoalphabetic'),
    path('playfair/', views.playfair, name='playfair'),
    path('hillcipher/', views.hillcipher, name='hillcipher'),
    path('extended_euclid', views.e_e, name='extended_euclid'),
    path('about/', views.about, name='about')
    
]
