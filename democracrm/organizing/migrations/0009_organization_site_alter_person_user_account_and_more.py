# Generated by Django 4.1.5 on 2023-01-08 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_organizationaccount_description_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('places', '0006_regiongroup_parent_sitegroup_parent'),
        ('organizing', '0008_organizationgroup_campaignmilestone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='places.site'),
        ),
        migrations.AlterField(
            model_name='person',
            name='user_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='PersonGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('org_account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.organizationaccount')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='organizing.persongroup', verbose_name='parent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='person',
            name='groups',
            field=models.ManyToManyField(to='organizing.persongroup'),
        ),
    ]
