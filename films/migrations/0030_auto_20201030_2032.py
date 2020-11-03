# Generated by Django 2.2.10 on 2020-10-30 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0029_auto_20201030_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, max_length=2500, null=True, verbose_name='Краткое содержание'),
        ),
        migrations.AlterField(
            model_name='person',
            name='biography',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Биография'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, choices=[('MALE', 'Мужской'), ('FEMALE', 'Женский')], max_length=15, null=True, verbose_name='Пол'),
        ),
    ]
