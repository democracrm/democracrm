# Generated by Django 4.1.4 on 2022-12-16 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organizing", "0004_campaign_legislation"),
    ]

    operations = [
        migrations.AddField(
            model_name="campaign",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="campaign",
            name="start_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
