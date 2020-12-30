from django.urls import path

from .views import addView, deleteView, index, homePageView, detail, searchView

urlpatterns = [
    path('', index, name='index'),
    path('homepage/', homePageView, name='home'),
    path('anecdotes/add/', addView, name='add'),
    path('anecdotes/delete/', deleteView, name='delete'),
    path('anecdotes/<int:anecdote_id>/', detail, name='detail'),
    path('anecdotes/search/', searchView, name='search')
]
