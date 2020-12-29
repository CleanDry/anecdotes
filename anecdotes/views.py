from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Anecdote


def index(request):
    return render(request, 'anecdotes/index.html')

@login_required
def homePageView(request):
    anecdotes = Anecdote.objects.filter(owner=request.user)
    return render(request, 'anecdotes/homepage.html', {'anecdotes': anecdotes})

def detail(request, anecdote_id):
    anecdote = get_object_or_404(Anecdote, pk=anecdote_id)
    return render(request, 'anecdotes/detail.html', {'anecdote':  anecdote})

def addView(request):
	text = request.POST.get('anecdote')
	a = Anecdote(owner=request.user, anecdote_text=text)
	a.save()
	return redirect('/homepage')

@login_required
def deleteView(request):
	a = Anecdote.objects.get(pk=request.POST.get('id'))

    # Vulnerability 1: Remove this to allow manufactured requests to delete other user's anecdotes 
	if a.owner != request.user:
		return redirect('/')

	a.delete()
	return redirect('/homepage')