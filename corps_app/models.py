from django.db import models
from datetime import datetime
from nysc_datacenter_backend.miscelaneous import RandomFileName
from cds_app.models import cds_model
from section_app.models import section_model
from nysc_datacenter_backend.formatChecker import file_size

class Members_app(models.Model):
    section = models.ForeignKey(section_model, on_delete=models.CASCADE)
    cds_group = models.ForeignKey(cds_model, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to=RandomFileName('images'),  blank=True, validators=[file_size])
    surname = models.CharField(max_length=200)
    othernames = models.CharField(max_length=500)
    statecode = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    call_up_no = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=10)
    state = models.CharField(max_length=100)
    lga = models.CharField(max_length=200)
    parent_name = models.CharField(max_length=200)
    address = models.TextField()
    parent_home_address = models.TextField()
    medical = models.IntegerField(default=0)
    name_next_kin = models.CharField(max_length=200)
    tel_next_kin = models.CharField(max_length=200)
    address_next_kin = models.TextField()
    date_registered_lga = models.CharField(max_length=100)
    self_tel = models.CharField(max_length=30)
    higher_institution = models.CharField(max_length=500)
    course_study = models.CharField(max_length=300)
    qualification = models.CharField(max_length=200)
    class_of_degree = models.CharField(max_length=200)
    name_ppa = models.CharField(max_length=200)
    address_ppa = models.TextField()
    cm_signature = models.ImageField(upload_to=RandomFileName('images'), blank=True, validators=[file_size])
    cm_signature_date = models.CharField(max_length=100)
    field_office_signature = models.ImageField(upload_to=RandomFileName('images'),  blank=True, validators=[file_size])
    field_office_signature_date = models.CharField(max_length=100, blank=True)
    for_office_only = models.TextField(blank=True)
    created_on = models.IntegerField(default=int(datetime.now().timestamp()))
    updated_on = models.IntegerField(default=int(datetime.now().timestamp()))

    def __str__(self):
        return self.statecode


