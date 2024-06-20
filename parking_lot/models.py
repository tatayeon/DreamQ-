from django.db import models

# Create your models here.

class ParkingLot(models.Model):  
    number = models.CharField(max_length=30)    # 주차장 번호
    content = models.TextField(blank=True)      # 주차장 정보 내용


    # head_image = models.ImageField(upload_to ='blog/images/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'{self.number}'

    def get_absolute_url(self):
        return f'/parking_lot/{self.pk}'