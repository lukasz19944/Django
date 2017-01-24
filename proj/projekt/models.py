from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Wizytowka(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    uczelnia = models.CharField(max_length=120)
    kierunek = models.CharField(max_length=60)
    telefon = models.CharField(max_length=15)
    email = models.EmailField(max_length=40)
    
    def utworz(self, imie, nazwisko, uczelnia, kierunek, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.uczelnia = uczelnia
        self.kierunek = kierunek
        self.telefon = telefon
        self.email = email
        
    