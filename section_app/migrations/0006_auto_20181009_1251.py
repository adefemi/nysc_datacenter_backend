# Generated by Django 2.1.2 on 2018-10-09 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section_app', '0005_auto_20181009_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section_model',
            name='created_on',
            field=models.IntegerField(default=1539085898),
        ),
        migrations.AlterField(
            model_name='section_model',
            name='year',
            field=models.CharField(max_length=50),
        ),
    ]
