# Generated by Django 2.1.2 on 2018-10-10 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corps_app', '0004_auto_20181009_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members_app',
            name='cds_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cds_app.cds_model'),
        ),
        migrations.AlterField(
            model_name='members_app',
            name='created_on',
            field=models.IntegerField(default=1539185444),
        ),
        migrations.AlterField(
            model_name='members_app',
            name='for_office_only',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='members_app',
            name='updated_on',
            field=models.IntegerField(default=1539185444),
        ),
    ]
