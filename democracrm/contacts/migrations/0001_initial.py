# Generated by Django 4.1.2 on 2022-11-25 18:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Contact Roles',
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name_prefix', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('name_suffix', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('personal_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('work_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('personal_fax', models.CharField(blank=True, max_length=255, null=True)),
                ('work_fax', models.CharField(blank=True, max_length=255, null=True)),
                ('personal_email', models.CharField(blank=True, max_length=255, null=True)),
                ('work_email', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contacts.contactrole')),
                ('site', models.ManyToManyField(to='places.site')),
            ],
            options={
                'verbose_name_plural': 'Contact Info',
            },
        ),
    ]
