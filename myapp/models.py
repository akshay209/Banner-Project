from django.db import models

# Create your models here.
class Banner(models.Model):
    position = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    end_time = models.TimeField()
    banner_type = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    image = models.ImageField(default='default.jpg',upload_to='images/')

class banner_images(models.Model):
    position = models.IntegerField()
    image = models.ImageField(default='default.jpg',upload_to='images/')
