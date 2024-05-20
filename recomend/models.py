from django.db import models
import os

# Create your models here.

class Attraction(models.Model):
    title = models.CharField(max_length = 30)

    type = models.CharField(max_length = 30)
    # Exciting
    # Walk
    # Child 
    # Photo
    # Experience
    # unscared
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank= True)

    Limit = models.TextField()

    Latitude = models.FloatField(blank= True, default=37.550254)

    Longitude = models.FloatField(blank= True, default=127.076493)

    def __str__(self):
        return f"[{self.title}] {self.type}"