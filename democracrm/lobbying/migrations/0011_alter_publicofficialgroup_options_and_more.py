# Generated by Django 4.1.4 on 2022-12-10 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lobbying", "0010_publicofficialgroup"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="publicofficialgroup",
            options={"verbose_name_plural": "Public Official Groups"},
        ),
        migrations.AlterField(
            model_name="publicofficial",
            name="role",
            field=models.CharField(
                choices=[
                    ("legislative", "Legislative"),
                    ("executive", "Executive"),
                    ("judicial", "Judicial"),
                    ("administrative", "Administrative"),
                    ("clerical", "Clerical"),
                ],
                default="legislative",
                max_length=100,
            ),
        ),
    ]
