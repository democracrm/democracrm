# Generated by Django 4.1.2 on 2022-11-14 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_contactinfo_options_alter_contactrole_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Note',
            new_name='Comment',
        ),
    ]