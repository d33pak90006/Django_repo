from django.shortcuts import render
from django.http import HttpResponse


guild = [

	{
		'Guild_Name' : 'Fairy Tail',
		'Member_Name' : 'Natsu Salamender',
		'Power' : 'Dragon Slayer',
		'Trained_By' : 'Igneel'
	},

	{
		'Guild_Name' : 'Fairy Tail',
		'Member_Name' : 'Gray Fullbuster',
		'Power' : 'Snow Prince',
		'Trained_By' : 'Jellal'
	},

	{
		'Guild_Name' : 'Fairy Tail',
		'Member_Name' : 'Lucy HeartFelia',
		'Power' : 'Gate Keeper',
		'Trained_By' : 'Makarov'
	}

]

def fairy(request):
	return HttpResponse('<h1>This is Fairy Tail School</h1>')

def display(request):
	
	disp =  {

		'post' : guild
	}


	return render(request,'fairy_tail/team_up.html',disp)