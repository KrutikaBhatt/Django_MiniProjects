# Generated by Django 3.1.2 on 2021-01-09 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convert_currency', '0007_auto_20210109_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='Result',
            field=models.FloatField(blank=True, null=True),
        ),
    ]