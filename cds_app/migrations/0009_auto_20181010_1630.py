# Generated by Django 2.1.2 on 2018-10-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cds_app', '0008_auto_20181009_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cds_model',
            name='created_on',
            field=models.IntegerField(default=1539185444),
        ),
        migrations.AlterField(
            model_name='cds_model',
            name='updated_on',
            field=models.IntegerField(default=1539185444),
        ),
    ]