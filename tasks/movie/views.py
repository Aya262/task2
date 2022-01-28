from django.shortcuts import render
from .forms import MovieForm
from .fillters import MovieFillter
from .models import Movie
# Create your views here.

def index(request):
    form=MovieForm()
    context={'form':form}
    return render(request,'index.html',context)


def home(request):
    movies={}
    filter=MovieFillter()
    allmovies=Movie.objects.all()
    if request.method=='POST':
        filter=MovieFillter(request.POST,queryset=allmovies)
        movies=filter.qs
        print(movies)
    context={'filter':filter,
    'movies':movies}
    return render(request,'home.html',context)