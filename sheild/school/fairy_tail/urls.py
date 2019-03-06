from django.urls import path
from . import views

urlpatterns = [
    
    path('tails/',views.fairy,name='fairy_school'),
    path('details/',views.display,name='guild_details')
]