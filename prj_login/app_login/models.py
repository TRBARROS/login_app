from django.db import models

# Create your models here.
class tblusers(models.Model):
    id = models.IntegerField(primary_key=True)
    strname = models.CharField(max_length=400)
    strmidname = models.CharField(max_length=400)
    strlastname = models.CharField(max_length=400)
    strlogin = models.CharField(max_length=400)
    strpassword = models.CharField(max_length=256)
    stremail = models.CharField(max_length=400)
    strphone = models.CharField(max_length=20)
    blnactive = models.BooleanField()
    dtmupdate = models.DateTimeField()