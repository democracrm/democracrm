# Generated by Django 4.1.4 on 2022-12-12 01:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("lobbying", "0015_alter_publicofficialrole_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="committee",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children",
                to="lobbying.committee",
                verbose_name="parent",
            ),
        ),
        migrations.CreateModel(
            name="CommitteeRole",
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
                ("is_leadership", models.BooleanField(default=False)),
                ("leadership_title", models.CharField(blank=True, max_length=255)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("chair", "Chair"),
                            ("vice-chair", "Vice-Chair"),
                            ("officio", "Ex-Officio"),
                            ("member", "Member"),
                        ],
                        default="member",
                        max_length=100,
                    ),
                ),
                ("service_start", models.DateField(blank=True, null=True)),
                ("service_end", models.DateField(blank=True, null=True)),
                ("notes", models.TextField(blank=True)),
                (
                    "public_official",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="lobbying.publicofficial",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Committee Roles",
            },
        ),
    ]