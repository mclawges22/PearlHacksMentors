# FILE: mentors/views.py

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	context = {'message':'Music is life, you gotta keep movin, now move!'}
	return render(request, 'base.html', context)