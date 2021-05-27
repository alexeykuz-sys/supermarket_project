"""
This function renders view of the index page
"""
from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return index page """

    return render(request, 'home/index.html')
