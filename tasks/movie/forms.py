from django.forms import ModelForm
from .models import Movie, Parser

class MovieForm(ModelForm):
    class Meta:
        model=Movie
        fields=['title','release_date','overview','popularity','vote_average','vote_count','video']

class ParserForm(ModelForm):
    class Meta:
        model=Parser
        fields=['file','type']


