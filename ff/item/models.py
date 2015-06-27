# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')

    def get_goods(self):
        return Good.objects.filter(category=self).order_by('-id')

    class Meta:
        verbose_name = 'Категорию товаров'        
        verbose_name_plural = 'Категория товаров'

    def __unicode__(self):
        return u'%s' % (self.name)


class Good(models.Model):
	category = models.ForeignKey(Category, related_name='categories', verbose_name='Категория')
	# name = models.CharField(max_length=250, verbose_name='Название')
	specifications = models.CharField(max_length=250, verbose_name='Характеристика')
	price = models.IntegerField(verbose_name='Цена',default=0)
	link = models.CharField(max_length=1250, verbose_name='Ссылка Яндекс маркета', blank=True)

	class Meta:
		verbose_name = 'Товар'        
		verbose_name_plural = 'Товары'

	def __unicode__(self):
		return u'{0} {1} ({2} руб)'.format(self.category, self.specifications, self.price)

