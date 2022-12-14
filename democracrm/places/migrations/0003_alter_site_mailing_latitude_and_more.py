# Generated by Django 4.1.2 on 2022-12-02 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_alter_location_options_alter_regiongroup_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='mailing_latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='mailing_longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='physical_latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='physical_longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
