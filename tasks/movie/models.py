from argparse import FileType
from django.db import models
from abc import ABC , abstractmethod
import pandas as pd
import json

# Create your models here.
class Movie(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=50)
    release_date=models.DateField()
    overview=models.TextField(max_length=1000,null=True,blank=True)
    popularity=models.FloatField()
    vote_average=models.FloatField()
    vote_count=models.IntegerField()
    video=models.BooleanField()

    def __str__(self):
        return str(self.title)


class Parser(models.Model):
    types=(('CSV','csv'),
    ('XLSX','xlsx'),
    ('xml','xml')
    )
    file=models.FileField(upload_to='Uploads/',max_length=254)
    type=models.CharField(choices=types,max_length=10)


class FileTypes(ABC):
    @abstractmethod
    def tojson(self,file):
        pass

class ExcelFile(FileTypes):
    def tojson(self, file):
        df=pd.read_excel(file,index_col=False)
        result=df.to_json(orient='records')
        parsed=json.loads(result)
        json_result=json.dumps(parsed,indent=4)
        return json_result


class CSVFile(FileTypes):
    def tojson(self, file):
        df=pd.read_csv(file)
        result=df.to_json(orient='records')
        parsed=json.loads(result)
        json_result=json.dumps(parsed,indent=4)
        return json_result

class XmlFile(FileType):
    def tojson(self, file):
        df=pd.read_xml(file)
        result=df.to_json(orient='records')
        parsed=json.loads(result)
        json_result=json.dumps(parsed,indent=4)
        return json_result
