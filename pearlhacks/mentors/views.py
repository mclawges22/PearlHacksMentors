# FILE: mentors/views.py

# Create your views here.
from django.shortcuts import render
from mentors.models import Mentor, Skill

def home(request):
	context = {
		'mentor_count': Mentor.objects.count(),
        'skill_count': Skill.objects.count(),
	}
	return render(request, 'base.html', context)