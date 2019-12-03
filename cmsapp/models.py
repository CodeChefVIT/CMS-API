from django.db import models

# Create your models here.
class Details(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    rfid = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=30, blank=True, default='')
    event_name = models.CharField(max_length=30, blank=True, default='')
    registration_number = models.CharField(max_length=30, blank=True, default='')
    phone_number = models.CharField(max_length=10)
    email = models.CharField(blank=True,max_length=253)
    class Meta:
        ordering = ['created']