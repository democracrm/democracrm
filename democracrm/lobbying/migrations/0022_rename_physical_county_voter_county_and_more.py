# Generated by Django 4.1.4 on 2022-12-14 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "lobbying",
            "0021_rename_physical_address_street_suffix_voter_physical_address_street_number_suffix",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="voter",
            old_name="physical_county",
            new_name="county",
        ),
        migrations.RenameField(
            model_name="voter",
            old_name="mailing_city",
            new_name="mailing_address_city",
        ),
        migrations.RenameField(
            model_name="voter",
            old_name="mailing_state",
            new_name="mailing_address_state",
        ),
        migrations.RenameField(
            model_name="voter",
            old_name="mailing_address_supplement",
            new_name="mailing_address_supplemental",
        ),
        migrations.RenameField(
            model_name="voter",
            old_name="mailing_zip_code",
            new_name="mailing_address_zip_code",
        ),
        migrations.RenameField(
            model_name="voter",
            old_name="physical_municipality",
            new_name="municipality",
        ),
        migrations.RenameField(
            model_name="voter",
            old_name="physical_city",
            new_name="physical_address_city",
        ),
        migrations.RenameField(
            model_name="voter",
            old_name="physical_address_supplement",
            new_name="physical_address_supplemental",
        ),
        migrations.RenameField(
            model_name="voter",
            old_name="physical_zip_code",
            new_name="physical_address_zip_code",
        ),
        migrations.RenameField(
            model_name="voter",
            old_name="physical_state",
            new_name="state",
        ),
        migrations.RemoveField(
            model_name="voter",
            name="physical_address_street_direction",
        ),
        migrations.AddField(
            model_name="voter",
            name="prefix_name",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Prefix Name"
            ),
        ),
        migrations.AddField(
            model_name="voter",
            name="suffix_name",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Suffix Name"
            ),
        ),
    ]
