from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.template import RequestContext, Context
from blog.models import movies, links
from .forms import RegistrationForm
import pandas as pd
from .recommendation import *

from imdb import IMDb

#import itertools
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
	#variables = Context({
	#	'user': request.user,
	#	})
	return render_to_response('index.html')#, variables)

def login_user(request):
	template = 'login.html'
	state="Please fill in your credentials"
	log = False
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				state = "Logged in!"
				log = True
				return HttpResponseRedirect('/search')
			else:
				state = "Not registered user"
		else:
			state = "Incorrect username or password!"
	variables = Context({
		'state': state,
		'log': log
		})
	return render_to_response(template, variables, RequestContext(request) )

def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')

#@login_required
def search(request):
	access = IMDb()
	query = "no results found"
	neighbors = []
	recommended = []
	results = []
	posters = []
	mvies = []
	show_results = False
	if request.GET:
		query = request.GET['query']
		results = movies.objects.filter (movie_name__icontains=query)[:10]
		show_results = True
#	titles = []
#	covers = []
	
#	for i in results:
	#	movie_id = links.objects.get(movie_id=i.movie_id)
	#	print('1')
	#	movie = access.get_movie(str(movie.imdb_id))
	#	titles.append(movie['title'])
	#	covers.append(movie['cover url'])
		print(results[0].movie_id)
		neighbors = recommend(results[0].movie_id)
		print(neighbors)
	
		for i in neighbors[:10]:
			recommends = movies.objects.get(movie_id=i)
			recommended.append(recommends)
			movie = access.get_movie(str(recommends.imdb_id))
			mvies.append(movie)
			print('8')
		
			poster = links.objects.get(movie_id=i)
			posters.append(poster)
			print('9')
		
	variables = Context({
		#'mvies': mvies,
		'posters': posters,
		'recommended': recommended,
		'results': results,
		'show_results': show_results
	})

	return render_to_response('search.html',variables, RequestContext(request))

def main(request):
	return render_to_response('main.html')

def reg_user(request):
	state= ""
	template = 'register.html'
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
				username = form.cleaned_data['username'],
				password = form.cleaned_data['password1'],
				email = form.cleaned_data['email']
			)
			return HttpResponseRedirect('/login')
		else:
			state = "Incorrect Credentials!"
	else:
		form = RegistrationForm()
	variables = RequestContext(request, {'form':form, 'state':state})
	return render_to_response('register.html', variables)

def movie(request):
	template = 'movie.html'
	query = ""
	if request.GET:
		query = request.GET['query']
		print(query)
		access = imdb.IMDb()
		movie = access.get_movie(str(query))

	variables = Context({
			'movie': movie
		})

	return render_to_response(template, variables)
