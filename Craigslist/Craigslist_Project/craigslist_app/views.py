from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'

# Create your views here.
def home(request):
    return render(request,"base.html")

def new_search(request):
    # search
    search = request.POST.get('search')
    response = requests.get(BASE_CRAIGSLIST_URL)
    data = response.text

    stuff_for_frontend = {
        'search': search,
    }

    return render(request,'craigslist_app/new_search.html',stuff_for_frontend)