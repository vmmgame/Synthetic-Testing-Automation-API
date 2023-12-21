# Generated by Django 5.0 on 2023-12-21 05:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_website_name_testresultmodel_website_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresultmodel',
            name='errors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, max_length=200, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='testresultmodel',
            name='webpage_size',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
