# Generated by Django 3.1.2 on 2020-10-17 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20201016_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='Combination_of_Primary_and_Highlight_Color',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Hectare_Squirrel_Number',
            field=models.IntegerField(blank=True),
        ),
    ]
