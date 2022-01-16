from django.db import models

# Create your models here.
class table(models.Model):
    long_num = models.FloatField(default = 113.4938)
    lat_num = models.FloatField(default = 53.5461)
    num = models.IntegerField(default = 1)  
    predicted = models.FloatField(default = 0.0)      