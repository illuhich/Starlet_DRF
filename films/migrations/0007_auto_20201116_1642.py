# Generated by Django 2.2.10 on 2020-11-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_persontranslation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(blank=True, related_name='movie_director', to='films.Person', verbose_name='Режиссеры'),
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together={('photo', 'birth_date')},
        ),
    ]
