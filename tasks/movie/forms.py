from django.forms import ModelForm
from .models import Movie

class MovieForm(ModelForm):
    class Meta:
        model=Movie
        fields=['title','release_date','overview','popularity','vote_average','vote_count','video']


