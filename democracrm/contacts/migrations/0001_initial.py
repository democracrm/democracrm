# Generated by Django 4.1.2 on 2022-12-02 11:49

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
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name_prefix', models.CharField(blank=True, max_length=50)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('name_suffix', models.CharField(blank=True, max_length=50)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('personal_phone', models.CharField(blank=True, max_length=255)),
                ('work_phone', models.CharField(blank=True, max_length=255)),
                ('mobile_phone', models.CharField(blank=True, max_length=255)),
                ('personal_fax', models.CharField(blank=True, max_length=255)),
                ('work_fax', models.CharField(blank=True, max_length=255)),
                ('personal_email', models.CharField(blank=True, max_length=255)),
                ('work_email', models.CharField(blank=True, max_length=255)),
                ('url', models.URLField(blank=True)),
                ('birthday', models.DateField(blank=True)),
                ('notes', models.TextField()),
                ('site', models.ManyToManyField(blank=True, to='places.site')),
            ],
            options={
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='ContactRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contact Roles',
            },
        ),
        migrations.CreateModel(
            name='ContactGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('contacts', models.ManyToManyField(blank=True, to='contacts.contact')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='contacts.contactgroup', verbose_name='parent')),
            ],
            options={
                'verbose_name_plural': 'Contact Groups',
            },
        ),
    ]
