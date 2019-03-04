from django.shortcuts import render
from django.http import HttpResponse
from .models import suitup




def team(request):
	return HttpResponse(render(request,'Revengers/ragnorok.html'))

def squad(request):
	
	destroyer = {
		'loki' : suitup.objects.all()
	}

	return HttpResponse(render(request,'Revengers/asgard.html',destroyer))


def widow(request):
	content = {

			'data' : suitup.objects.all()
	}

			
	return render(request,'Revengers/winter.html',content,{'title':'Fury'})

