# Generated by Django 2.1.2 on 2018-10-09 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corps_app', '0003_auto_20181009_1251'),
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
            field=models.IntegerField(default=1539085898),
        ),
        migrations.AlterField(
            model_name='members_app',
            name='updated_on',
            field=models.IntegerField(default=1539085898),
        ),
    ]
