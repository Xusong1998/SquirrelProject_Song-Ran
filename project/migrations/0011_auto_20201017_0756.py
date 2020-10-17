# Generated by Django 3.1.2 on 2020-10-17 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_auto_20201017_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='Above_Ground_Sighter_Measurement',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Age',
            field=models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Approaches',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Chasing',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Climbing',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Color_notes',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Combination_of_Primary_and_Highlight_Color',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Eating',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Foraging',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Hectare',
            field=models.CharField(blank=True, choices=[('AM', 'AM'), ('PM', 'PM')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Indifferent',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Kuks',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Lat_Long',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Moans',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Other_Activities',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Other_Interactions',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Primary_Fur_Color',
            field=models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Quaas',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Running',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Runs_from',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Specific_Location',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Tail_flags',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Tail_twitches',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
