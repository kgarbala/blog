# -*- coding: utf-8 -*-
from django.db import models

class Category(models.Model):
    name = models.CharField(max_lenght=255, verbose_name='Index')
    slug = models.SlugField(max_lenght=255, unique=True, verbose_name='Odnosnik')
    icon = models.ImageField(upload_to='icons', verbose_name='Ikona kategorii', blank=True)
    class Meta:
	verbose_name = 'Kategoria'
	verbose_name_plural = 'Kategorie'
    def __str__(self):
	return self.name
    def __unicode__(self):
	return self.name
    class News():
	category = models.ManyToManyField(Category, verbose_name='Kategorie')
	title = models.CharField(max_lenght=255, verbose_name='Tytul')
	text = models.TextField(verbose_name='Tresc')
	date = models.DateTimeField(verbose_name='Data dodania')
	wykop = models.CharField(max_lenght=255, verbose_name='Wykop', blank=True)
	class Meta:
	    verbose_name = "Wiadomosc"
	    verbose_name_plural = 'Wiadomosci'
	    def __str__(self):
		return self.title
	    def __unicode__(self):
		return self.title
	    def get_absolute_url(self):
		return '/news' + self.slug + '/'
