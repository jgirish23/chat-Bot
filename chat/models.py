from django.db import models
# Create your models here.

class Chats(models.Model):
    Username=models.CharField(max_length=255,blank=False)
    Text = models.CharField(max_length=255,blank=False)
    Text_order = models.IntegerField(blank=False)
    Check=models.BooleanField(blank=False)
