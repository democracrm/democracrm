# Generated by Django 4.0.6 on 2022-10-08 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lobbying', '0002_politicalsubdivision_alter_publicofficial_is_elected'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicofficial',
            name='subdivision',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='lobbying.politicalsubdivision'),
        ),
    ]