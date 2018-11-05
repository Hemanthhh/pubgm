from django.db import models

# Create your models here.

class Data(models.Model):
    name = models.CharField(max_length = 50)
    whatsapp = models.IntegerField()
    paytm = models.IntegerField()
    pubg_uid = models.IntegerField()
    pubg_uname = models.CharField(max_length = 50)

    def __str__(self):
        return self.name