# Generated by Django 4.1.5 on 2023-01-13 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizing', '0010_alter_campaignmilestone_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relationship',
            old_name='organization',
            new_name='org_subject',
        ),
        migrations.RenameField(
            model_name='relationship',
            old_name='person',
            new_name='person_subject',
        ),
        migrations.AddField(
            model_name='organization',
            name='relationships',
            field=models.ManyToManyField(blank=True, to='organizing.relationship'),
        ),
        migrations.AddField(
            model_name='person',
            name='relationships',
            field=models.ManyToManyField(blank=True, to='organizing.relationship'),
        ),
        migrations.AlterField(
            model_name='person',
            name='groups',
            field=models.ManyToManyField(blank=True, to='organizing.persongroup'),
        ),
    ]
