from cgitb import lookup
import django_filters
from .models import Movie
from django_filters import DateFilter

class MovieFillter(django_filters.FilterSet):

    #release_year=django_filters.NumberFilter(field_name='release_date',lookup_expr='year')
    title=django_filters.CharFilter(field_name='title',lookup_expr='icontains')
    overview=django_filters.CharFilter(field_name='overview',lookup_expr='icontains')
    release_date=DateFilter(field_name='release_date',lookup_expr='gte')
    popularity=django_filters.NumberFilter(field_name='popularity',lookup_expr='gte')
    vote_average=django_filters.NumberFilter(field_name='vote_average',lookup_expr='gte')
    vote_count=django_filters.NumberFilter(field_name='vote_count',lookup_expr='gte')
    #release_year__lt=django_filters.NumberFilter(field_name='release_date',lookup_expr='year__lt')

    class Meta:
        model=Movie
        fields=['video']
