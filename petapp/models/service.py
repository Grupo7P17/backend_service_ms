from django.db import models

class Service(models.Model):
    id    = models.AutoField('id',primary_key=True)
    service  = models.CharField('Service', max_length=100)
    cost  = models.IntegerField('Cost',)
    days = models.IntegerField('Days')
    category   = models.CharField('category', max_length=50)