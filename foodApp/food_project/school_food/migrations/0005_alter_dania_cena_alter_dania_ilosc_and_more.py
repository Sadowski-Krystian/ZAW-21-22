# Generated by Django 4.0.4 on 2022-04-26 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_food', '0004_alter_dania_ilosc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dania',
            name='cena',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='dania',
            name='ilosc',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='dania',
            name='kategoria',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='dania',
            name='nazwa',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='dania',
            name='opis',
            field=models.CharField(max_length=255),
        ),
    ]
