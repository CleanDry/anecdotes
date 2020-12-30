from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import sqlite3
from .models import Anecdote


def index(request):
    return render(request, 'anecdotes/index.html')

@login_required
def homePageView(request):
	anecdotes = Anecdote.objects.filter(owner=request.user)
	return render(request, 'anecdotes/homepage.html', {'anecdotes': anecdotes})

@login_required
def detail(request, anecdote_id):
    anecdote = get_object_or_404(Anecdote, pk=anecdote_id)

	# OWASP vulnerability 3: Sensitive data exposure. Fix:
	# if anecdote.owner != request.user:
	#	return redirect('/')

    return render(request, 'anecdotes/detail.html', {'anecdote':  anecdote})

@login_required
def addView(request):
	a = Anecdote(owner=request.user, anecdote_text=request.POST.get('anecdote'))
	a.save()
	return redirect('/homepage')

@login_required
# OWASP vulnerability 6: Security misconfiguration. 
@csrf_exempt
def deleteView(request):
	a = Anecdote.objects.get(pk=request.POST.get('id'))

    # OWASP vulnerability 5: Manufactured requests allowed to delete other user's anecdotes 
	# Fix:
	# if a.owner != request.user:
	#	return redirect('/')

	a.delete()
	return redirect('/homepage')

@login_required
def searchView(request):
	found_users = []
	query = request.POST.get('query')
	conn = sqlite3.connect('./db.sqlite3')
	cursor = conn.cursor()

	# OWASP vulnerability 1: SQL Injection. Fix: Use framework's Models correctly.

	parsed_query = "SELECT auth_user.username FROM auth_user, anecdotes_anecdote WHERE auth_user.id = Anecdotes_anecdote.owner_id AND Anecdotes_anecdote.anecdote_text LIKE '%%%s%%'" % (query)
	response = cursor.execute(parsed_query).fetchall()
	for r in response:
		found_users.append(r[0])
	return render(request, 'anecdotes/search.html', {'found_users': found_users})

	# Possible injections might be structured as something like:
	# bird%' union select auth_user.username FROM auth_user where id like '%