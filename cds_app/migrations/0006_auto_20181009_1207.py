# Generated by Django 2.1.2 on 2018-10-09 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cds_app', '0005_auto_20181003_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cds_model',
            name='created_on',
            field=models.IntegerField(default=1539083254),
        ),
        migrations.AlterField(
            model_name='cds_model',
            name='updated_on',
            field=models.IntegerField(default=1539083254),
        ),
    ]
