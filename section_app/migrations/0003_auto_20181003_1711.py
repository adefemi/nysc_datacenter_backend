# Generated by Django 2.1.2 on 2018-10-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section_app', '0002_auto_20181003_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section_model',
            name='created_on',
            field=models.IntegerField(default=1538583065),
        ),
    ]