# Generated by Django 4.1.2 on 2022-11-14 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobbying', '0017_campaign_is_complete'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campaign',
            options={'ordering': ['priority']},
        ),
        migrations.AlterField(
            model_name='campaign',
            name='priority',
            field=models.IntegerField(choices=[(5, 'Top'), (4, 'High'), (3, 'Medium'), (2, 'Low'), (1, 'None')], default=3),
        ),
    ]