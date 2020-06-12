# Generated by Django 2.2.10 on 2020-05-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0009_auto_20200520_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='age_limit',
            field=models.PositiveIntegerField(default=0, verbose_name='Возрастное ограничение'),
        ),
        migrations.AlterField(
            model_name='film',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Краткое содержание'),
        ),
        migrations.AlterField(
            model_name='film',
            name='tagline',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Слоган'),
        ),
    ]
