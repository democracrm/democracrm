# Generated by Django 4.1.4 on 2022-12-14 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lobbying", "0024_voter_data_export_date_voter_last_election_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="voter",
            name="political_party_code",
            field=models.CharField(default="O", max_length=50),
            preserve_default=False,
        ),
    ]
