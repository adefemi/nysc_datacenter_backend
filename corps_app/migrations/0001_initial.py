# Generated by Django 2.1.2 on 2018-10-03 16:11

from django.db import migrations, models
import django.db.models.deletion
import nysc_datacenter_backend.miscelaneous


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('section_app', '0003_auto_20181003_1711'),
        ('cds_app', '0005_auto_20181003_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members_app',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(default='null', upload_to=nysc_datacenter_backend.miscelaneous.RandomFileName('images'))),
                ('surname', models.CharField(max_length=200)),
                ('othernames', models.CharField(max_length=500)),
                ('statecode', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=10)),
                ('call_up_no', models.CharField(max_length=100)),
                ('marital_status', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=100)),
                ('lga', models.CharField(max_length=200)),
                ('parent_name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('parent_home_address', models.TextField()),
                ('medical', models.IntegerField(default=0)),
                ('name_next_kin', models.CharField(max_length=200)),
                ('tel_next_kin', models.CharField(max_length=200)),
                ('address_next_kin', models.TextField()),
                ('date_registered_lga', models.CharField(max_length=100)),
                ('self_tel', models.CharField(max_length=30)),
                ('higher_institution', models.CharField(max_length=500)),
                ('course_study', models.CharField(max_length=300)),
                ('qualification', models.CharField(max_length=200)),
                ('class_of_degree', models.CharField(max_length=200)),
                ('name_ppa', models.CharField(max_length=200)),
                ('address_ppa', models.TextField()),
                ('cm_signature', models.ImageField(default='null', upload_to=nysc_datacenter_backend.miscelaneous.RandomFileName('images'))),
                ('cm_signature_date', models.CharField(max_length=100)),
                ('field_office_signature', models.ImageField(default='null', upload_to=nysc_datacenter_backend.miscelaneous.RandomFileName('images'))),
                ('field_office_signature_date', models.CharField(max_length=100)),
                ('for_office_only', models.TextField()),
                ('created_on', models.IntegerField(default=1538583065)),
                ('updated_on', models.IntegerField(default=1538583065)),
                ('cds_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cds_app.cds_model')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='section_app.section_model')),
            ],
        ),
    ]
