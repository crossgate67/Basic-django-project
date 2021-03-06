# Generated by Django 4.0.1 on 2022-05-28 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(max_length=50, verbose_name='Filmin süresi'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_type',
            field=models.CharField(max_length=60, verbose_name='Filmin türü'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Filmin Adı'),
        ),
    ]
