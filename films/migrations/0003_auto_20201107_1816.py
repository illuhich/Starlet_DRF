# Generated by Django 2.2.10 on 2020-11-07 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_auto_20201105_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genretranslation',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='orig_title',
            field=models.CharField(max_length=70, verbose_name='Оригинальное название'),
        ),
    ]
