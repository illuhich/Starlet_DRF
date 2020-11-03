# Generated by Django 2.2.10 on 2020-10-28 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0022_auto_20201028_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='age_limit',
            field=models.CharField(blank=True, default=0, max_length=10, null=True, verbose_name='Возрастное ограничение'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='orig_title',
            field=models.CharField(blank=True, max_length=70, null=True, verbose_name='Оригинальное название'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='movie/posters/', verbose_name='Постер'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата выхода'),
        ),
    ]
