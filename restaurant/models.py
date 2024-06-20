from django.db import models

# Create your models here.

class Post(models.Model):  
    title = models.CharField(max_length=30)
    content = models.TextField()

    menu_image = models.ImageField(upload_to ='blog/images/restaurants', blank=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/restaurant/{self.pk}'
    

class Restaurant(models.Model):  
    category = models.CharField(max_length=20)  # 한식/중식/카페/간식 등
    name = models.CharField(max_length=30)      # 식당명   
    content = models.TextField()                # 식당 설명
    photo = models.ImageField(upload_to ='blog/images/restaurants', blank=True)
    menu = models.CharField(max_length=30)      # 메뉴명
    price = models.IntegerField()               # 메뉴 가격
    menu_image = models.ImageField(upload_to ='blog/images/restaurants', blank=True)    # 메뉴별 사진
    tel = models.CharField(max_length=20)       # 식당 번호
    # location 추가하기
    

    def __str__(self):
        return f'[{self.pk}] {self.name}'

    def get_absolute_url(self):
        return f'/restaurant/{self.pk}'