# Generated by Django 4.1.2 on 2022-11-20 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobbying', '0008_alter_legislation_campaign_delete_campaign_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicoffice',
            name='seats',
            field=models.IntegerField(default=1),
        ),
    ]