# Generated by Django 3.2.11 on 2022-01-28 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_movie_overview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=254, upload_to='Uploads')),
                ('type', models.CharField(choices=[('CSV', 'csv'), ('XLSX', 'xlsx'), ('xml', 'xml')], max_length=10)),
            ],
        ),
    ]
