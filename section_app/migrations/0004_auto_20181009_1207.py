# Generated by Django 2.1.2 on 2018-10-09 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section_app', '0003_auto_20181003_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='section_model',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='section_model',
            name='created_on',
            field=models.IntegerField(default=1539083254),
        ),
    ]
