# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from item.models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from django.core.urlresolvers import reverse
from allauth.account.models import EmailAddress
from operator import itemgetter
import datetime
from django.db.models import Count, Min, Sum
from django.db import connection
from django.core.mail import send_mail
import json


def index(request):
	if not request.user.is_authenticated():
		return redirect('/accounts/login/')

	return redirect('/price/')

def signup(request):
	return render_to_response('signup.html')

def about(request):
	return render_to_response('about.html')

def nocode(request):
	return render_to_response('nocode.html')

def forgotpass(request):
	return render_to_response('forgotpass.html')

def rules(request):
	return render_to_response('rules.html')

def price(request):
	if not request.user.is_authenticated():
		return redirect('/accounts/login/')
	categories = Category.objects.all()
	return render_to_response('price.html',{'categories':categories})

def thanks(request):
	if not request.user.is_authenticated():
		return redirect('/accounts/login/')
	return render_to_response('thanks.html')

def nogoods(request):
	if not request.user.is_authenticated():
		return redirect('/accounts/login/')
	return render_to_response('nogoods.html')

def cash(request):
	if not request.user.is_authenticated():
		return redirect('/accounts/login/')
	return render_to_response('cash.html')

def review(request):
	return render_to_response('review.html')

def invite(request):
	if not request.user.is_authenticated():
		return redirect('/accounts/login/')
	return render_to_response('invite.html')

def faq(request):
	if not request.user.is_authenticated():
		return redirect('/accounts/login/')
	faq = Faq.objects.all()
	return render_to_response('faq.html',{'faq':faq})

def order(request,goods):
	if not request.user.is_authenticated():
		return redirect('/accounts/login/')

	ids_goods = goods.split('_')
	goods = Good.objects.filter(id__in=ids_goods)
	summ_order = 0
	for good in goods:
		summ_order += int(good.price)
	return render_to_response('order.html',{"goods": goods,"summ_order":summ_order})

def email_send(request):
	if not request.user.is_authenticated():
		return redirect('/accounts/login/')
	if request.method == 'POST':
		data_goods = request.POST.get('data_goods', '')
		phone = str(request.POST.get('phone', ''))

		list_goods = json.loads(data_goods)
		message1 = u'Создан заказ<br/><br/><table style="padding:5px; border:1px solid #ccc;"><tr><td style="padding:10px">  id  </td><td style="padding:10px">  Наименование  </td><td style="padding:10px">  Кол-во  </td><td style="padding:10px">  Цена за ед.  </td><td style="padding:10px">  Сумма  </td></tr>'
		summ_itog = 0
		for good in list_goods:
			# this_good = Good.objects.filter(id=good['id'])
			# for this in this_good:
				# summ_good=this.price*int(good['count'])
			summ_itog += int(good['count'])*int(good['price'])
			message1 += u'<tr><td style="padding:10px">{0}</td><td style="padding:10px">{1}</td><td style="padding:10px">{2}</td><td style="padding:10px">{3}</td><td style="padding:10px">{4}</td></tr>'.format(good['id'],good['name'],good['count'],good['price'],int(good['count'])*int(good['price']))
			
			


		message1 += u'</table><br/> Итого {0} рублей<br/> Телефон заказчика {1}'.format(summ_itog,phone)
		subject = u'Заявка  - {0}'.format(phone)
		message = u'{0}'.format(phone)

		send_mail(subject, message, 'ddruzyam@mail.ru', ['makarow.dmitry@gmail.com'], fail_silently=False, html_message=message1)
		return HttpResponse()

# summ_itog = 0
		# for good in list_goods:
		# 	summ_itog += int(good['count'])*int(good['price'])
		# 	message1 += u'<tr><td style="padding:5px; border:1px solid #ccc;">{0}</td><td style="padding:5px; border:1px solid #ccc;">{1}</td><td style="padding:5px; border:1px solid #ccc;">{2}</td><td style="padding:5px; border:1px solid #ccc;">{3}</td><td style="padding:5px; border:1px solid #ccc;">{4}</td></tr>'.format(good['id'],good['name'],good['count'],good['price'],int(good['count'])*int(good['price']))
			
			

		# message1 += u

	