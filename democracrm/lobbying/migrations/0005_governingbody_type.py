# Generated by Django 4.1.2 on 2022-11-13 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobbying', '0004_governingbody_geographic_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='governingbody',
            name='type',
            field=models.CharField(choices=[('legislative', 'Legislative'), ('executive', 'Executive'), ('judicial', 'Judicial')], default='legislative', max_length=255),
            preserve_default=False,
        ),
    ]