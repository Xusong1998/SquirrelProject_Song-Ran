# Generated by Django 3.1.2 on 2020-10-18 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20201017_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='Hectare',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Location',
            field=models.CharField(blank=True, choices=[('Above Ground', 'Above Ground'), ('Ground Plane', 'Ground Plane')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Shift',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], max_length=10),
        ),
    ]
