from django.shortcuts import render
from django.http import HttpResponse



temp_list  = [

	{
		'Name' : 'Bucky Barnes',
		'Place' : 'Brooklyn',
		'Friend' : 'Steve Rogers',
		'Alias' : 'Winter Soldier'
	},

	{
		'Name' : 'Steve Rogers',
		'Place' : 'Brooklyn',
		'Friend' : 'Bucky Barnes',
		'Alias' : 'Captain America'
	}

]

thor = [

	{
		'Planet' : 'Asgard',
		'Realm' : 'Jonatheium',
		'King' : 'Bhor',
		'Queen' : 'Hela'
	}

]

def team(request):
	return HttpResponse(render(request,'Revengers/ragnorok.html'))

def squad(request):
	
	destroyer = {
		'loki' : thor
	}

	return HttpResponse(render(request,'Revengers/asgard.html',destroyer))


def widow(request):
	content = {

			'data' : temp_list
	}

			
	return render(request,'Revengers/winter.html',content,{'title':'Fury'})

