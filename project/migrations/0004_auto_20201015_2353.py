# Generated by Django 3.1.2 on 2020-10-15 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_squirrel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='Approaches',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Chasing',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Climbing',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Eating',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Foraging',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Indifferent',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Kuks',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Moans',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Quaas',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Running',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Runs_from',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Tail_flags',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Tail_twitches',
            field=models.BooleanField(),
        ),
    ]
