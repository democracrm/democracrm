# Generated by Django 4.1.2 on 2022-11-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobbying', '0013_socialmediaaccount_voter_email_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediaaccount',
            name='platform',
            field=models.CharField(choices=[('twitter', 'Twitter')], max_length=255),
        ),
    ]
