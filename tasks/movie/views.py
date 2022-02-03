from django.shortcuts import render
from .forms import MovieForm ,ParserForm
from .fillters import MovieFillter
from .models import *
import pandas as pd
import json
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
'''
def parser(request):
    json_result={}
    form=ParserForm()
    filetype={}
    #df=pd.DataFrame()
    if request.method=='POST':
        type=request.POST['type']
        filename=request.FILES['file']
        if type=='XLSX':
            filetype=ExcelFile()
            #df=pd.read_excel(filename,index_col=False)
        elif type=='CSV':
            df=pd.read_csv(filename)
        elif type=='xml':
            df=pd.read_xml(filename)
        result=df.to_json(orient='records')
        parsed=json.loads(result)
        json_result=json.dumps(parsed,indent=4)
    context={'form':form,
             'json_result':json_result}
    return render(request,'parser.html',context)
'''

def converToJson(request):
    json_result={}
    form=ParserForm()
    filetype=None
    if request.method=='POST':
        type=request.POST['type']
        filename=request.FILES['file']
        if type=='XLSX':
            filetype=ExcelFile()
        elif type=='CSV':
            filetype=CSVFile()
        elif type=='xml':
            filetype=XmlFile()
        json_result=filetype.tojson(filename)

    context={'form':form,
             'json_result':json_result}
    return render(request,'parser.html',context)
