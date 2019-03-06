from django.urls import path
from . import views

urlpatterns = [
    path('', views.team, name='revengers-team'),
    path('squad/',views.squad, name='new_squad'),
    path('black/',views.widow, name='natasha')
]