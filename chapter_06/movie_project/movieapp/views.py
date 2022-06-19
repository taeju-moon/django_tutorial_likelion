from django.shortcuts import render
import requests
import json
from .forms import SearchForm
from . import store_key

my_key = store_key.my_key

def home(request):
    print("home")
    if request.method == "POST":
        form = SearchForm(request.POST)
        searchWord = request.POST.get("search")
        if form.is_valid():
            url = f'https://api.themoviedb.org/3/search/movie?api_key={my_key}&query={searchWord}'
            response = requests.get(url)
            resdata = json.loads(response.text)["results"]
            form = SearchForm()
            return render(request, "search.html", {"resdata":resdata, "form":form})
    else:
        form = SearchForm()
        url = f'https://api.themoviedb.org/3/trending/tv/week?api_key={my_key}'
        response = requests.get(url)
        resdata = json.loads(response.text)["results"]
        return render(request, "index.html", {'resdata':resdata, "form":form})

def detail(request, movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={my_key}'
    response = requests.get(url)
    movie = response.text
    resdata = json.loads(movie)
    return render(request, "detail.html", {"resdata":resdata})
