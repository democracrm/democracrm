# Generated by Django 4.1.2 on 2022-11-25 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
        ('places', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationaccount',
            name='primary_contact',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='contacts.contactinfo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizationaccount',
            name='territory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='places.boundary'),
            preserve_default=False,
        ),
    ]