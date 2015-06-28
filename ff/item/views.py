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

def order(request):
	if not request.user.is_authenticated():
		return redirect('/accounts/login/')
	return render_to_response('order.html')