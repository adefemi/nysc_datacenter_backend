from django.db import models
from datetime import datetime

class section_model(models.Model):
    year = models.CharField(max_length=50)
    batch = models.CharField(max_length=2)
    active = models.BooleanField(default=False)
    created_on = models.IntegerField(default=int(datetime.now().timestamp()))

    def __str__(self):
        return self.year + " " + self.batch
