from django.urls import path

from .views import addView, deleteView, index, homePageView, detail

urlpatterns = [
    path('', index, name='index'),
    path('homepage/', homePageView, name='home'),
    path('homepage/add/', addView, name='add'),
    path('homepage/delete/', deleteView, name='delete'),
    path('<int:anecdote_id>/', detail, name='detail')
]
