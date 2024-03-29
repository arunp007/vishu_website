from django.urls import path
from.import views

urlpatterns = [
    path('vishu', views.vishu, name='home'),
    path('astro', views.astro, name='future'),
    path('ashwathi', views.ashwathi, name='ashwathi'),
    path('bharani', views.bharani, name='bharani'),
    path('karthika', views.karthika, name='karthika'),
    path('rohini', views.rohini, name='rohini'),
    path('magayiram', views.magayiram, name='magayiram'),
    path('thiruvathira', views.thiruvathira, name='thiruvathira'),
    path('punardam', views.punardam, name='punardam'),
    path('pooyam', views.pooyam, name='pooyam'),
    path('aayilyam', views.aayilyam, name='aayilyam'),
    path('magham', views.magham, name='magham'),
    path('pooram', views.pooram, name='pooram'),
    path('uthram', views.uthram, name='uthram'),
    path('atham', views.atham, name='atham'),
    path('chithira', views.chithira, name='chithira'),
    path('chothi', views.chothi, name='chothi'),
    path('vishagham', views.vishagham, name='vishagham'),
    path('anizham', views.anizham, name='anizham'),
    path('threketta', views.threketta, name='threketta'),
    path('moolam', views.moolam, name='moolam'),
    path('pooradam', views.pooradam, name='pooradam'),
    path('uthradam', views.uthradam, name='uthradam'),
    path('thiruvonam', views.thiruvonam, name='thiruvonam'),
    path('avittam', views.avittam, name='avittam'),
    path('chadayam', views.chadayam, name='chadayam'),
    path('puruttathi', views.puruttathi, name='puruttathi'),
    path('uthrattathi', views.uthrattathi, name='uthrattathi'),
    path('revathi', views.revathi, name='revathi'),
]