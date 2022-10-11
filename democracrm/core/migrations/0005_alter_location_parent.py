# Generated by Django 4.0.6 on 2022-10-04 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_site_latitude_alter_site_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.location'),
        ),
    ]