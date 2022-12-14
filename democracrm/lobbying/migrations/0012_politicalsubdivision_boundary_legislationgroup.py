# Generated by Django 4.1.4 on 2022-12-10 18:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0005_alter_location_options_alter_sitegroup_options"),
        ("lobbying", "0011_alter_publicofficialgroup_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="politicalsubdivision",
            name="boundary",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.RESTRICT,
                to="places.boundary",
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="LegislationGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("notes", models.TextField(blank=True)),
                (
                    "legislation",
                    models.ManyToManyField(blank=True, to="lobbying.legislation"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
