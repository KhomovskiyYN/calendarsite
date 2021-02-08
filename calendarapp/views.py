from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from calendarapp import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#=================================================================================================
# Education Universe

def week(request):
	loginId = 1
	calendar = getPersonalCalendar(loginId)
	week = calendar.currentWeek()
	template = loader.get_template('calendar/week.html')
	context = { 'week': week } 
	return HttpResponse(template.render(context, request))
