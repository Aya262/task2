from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Movie


# Register your models here.


class MovieAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Movie,MovieAdmin)