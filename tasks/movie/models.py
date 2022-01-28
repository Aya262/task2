from django.db import models

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
