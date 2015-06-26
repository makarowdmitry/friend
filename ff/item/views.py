# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
	return render_to_response('login.html')

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