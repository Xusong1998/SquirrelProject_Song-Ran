# Generated by Django 3.1.2 on 2020-10-17 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20201017_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='Hectare_Squirrel_Number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
