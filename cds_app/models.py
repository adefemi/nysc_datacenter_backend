from django.db import models
from datetime import datetime

class cds_model(models.Model):
    title = models.CharField(max_length=50)
    titleShort = models.CharField(max_length=10)
    created_on = models.IntegerField(default=int(datetime.now().timestamp()))
    updated_on = models.IntegerField(default=int(datetime.now().timestamp()))

    def __str__(self):
        return self.titleShort

