# Generated by Django 4.1.2 on 2022-11-17 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lobbying', '0002_alter_platform_organization'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrganizationAccount',
        ),
    ]