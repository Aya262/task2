from django.urls import path
from .views import index ,home ,parser
urlpatterns = [
    path('',home,name='home'),
    path('parse/',parser,name='parser')
]