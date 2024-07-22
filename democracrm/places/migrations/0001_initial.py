# Generated by Django 4.1.2 on 2022-12-02 11:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boundary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('level', models.CharField(choices=[('nation', 'Nation'), ('state', 'State'), ('county', 'County'), ('municipality', 'Municipality')], max_length=255)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='places.boundary', verbose_name='parent')),
            ],
            options={
                'verbose_name_plural': 'Boundaries',
            },
        ),
        migrations.CreateModel(
            name='RegionGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('overlapping_enabled', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiteGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('has_physical_address', models.BooleanField(default=False)),
                ('physical_street_number', models.CharField(blank=True, max_length=10)),
                ('physical_street_direction', models.CharField(blank=True, max_length=10)),
                ('physical_street_name', models.CharField(blank=True, max_length=255)),
                ('physical_street_suffix', models.CharField(blank=True, max_length=100)),
                ('physical_unit_number', models.CharField(blank=True, max_length=50)),
                ('physical_city', models.CharField(blank=True, max_length=255)),
                ('physical_state', models.CharField(blank=True, max_length=255)),
                ('physical_zip_code', models.CharField(blank=True, max_length=10)),
                ('physical_county', models.CharField(blank=True, max_length=255)),
                ('physical_latitude', models.FloatField(blank=True)),
                ('physical_longitude', models.FloatField(blank=True)),
                ('has_mailing_address', models.BooleanField(default=False)),
                ('mailing_street_number', models.CharField(blank=True, max_length=10)),
                ('mailing_street_direction', models.CharField(blank=True, max_length=10)),
                ('mailing_street_name', models.CharField(blank=True, max_length=255)),
                ('mailing_street_suffix', models.CharField(blank=True, max_length=100)),
                ('mailing_unit_number', models.CharField(blank=True, max_length=50)),
                ('mailing_po_box', models.CharField(blank=True, max_length=255)),
                ('mailing_city', models.CharField(blank=True, max_length=255)),
                ('mailing_state', models.CharField(blank=True, max_length=255)),
                ('mailing_zip_code', models.CharField(blank=True, max_length=10)),
                ('mailing_county', models.CharField(blank=True, max_length=255)),
                ('mailing_latitude', models.FloatField(blank=True)),
                ('mailing_longitude', models.FloatField(blank=True)),
                ('group', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='places.sitegroup')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('boundaries', models.ManyToManyField(blank=True, to='places.boundary')),
                ('group', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='places.regiongroup')),
            ],
            options={
                'verbose_name_plural': 'Regions',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('unit', models.CharField(blank=True, max_length=255)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='places.location', verbose_name='parent')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='places.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]