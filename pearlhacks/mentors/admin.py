#!/usr/bin/env python

from django.contrib import admin
from mentors.models import Mentor

class MentorAdmin(admin.ModelAdmin):
	search_fields = ('firstName', 'lastName', 'company',)

admin.site.register(Mentor, MentorAdmin)
