# Generated by Django 2.1.2 on 2018-10-03 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cds_app', '0003_auto_20181003_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cds_model',
            name='created_on',
            field=models.IntegerField(default=1538582390),
        ),
        migrations.AlterField(
            model_name='cds_model',
            name='updated_on',
            field=models.IntegerField(default=1538582390),
        ),
    ]
