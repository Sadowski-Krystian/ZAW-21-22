# Generated by Django 4.0.4 on 2022-04-26 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_food', '0006_dania_create_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='dania',
            name='modify_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='dania',
            name='create_time',
            field=models.DateTimeField(),
        ),
    ]
