# Generated by Django 2.1.2 on 2018-10-03 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cds_app', '0002_auto_20181003_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cds_model',
            name='created_on',
            field=models.IntegerField(default=1538581423),
        ),
        migrations.AlterField(
            model_name='cds_model',
            name='updated_on',
            field=models.IntegerField(default=1538581423),
        ),
    ]
