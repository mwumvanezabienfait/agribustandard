from datetime import datetime

from django.db import models

# Create your models here.


# class Crop(models.Model):
#     names: models.CharField(max_length=255,)
#     quantity: models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.names

class Crop(models.Model):
    sessiondId = models.CharField(max_length=255, null=True)
    serviceCode = models.CharField(max_length=255, null=True)
    phoneNumber = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    sizeOfland = models.CharField(max_length=255)
    names = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=255)
    created_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.phoneNumber


