# Generated by Django 4.0.6 on 2022-10-08 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PublicOfficial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix_name', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('suffix_name', models.CharField(blank=True, max_length=50, null=True)),
                ('is_elected', models.BooleanField()),
                ('official_type', models.CharField(default='Legislator', max_length=100)),
            ],
        ),
    ]