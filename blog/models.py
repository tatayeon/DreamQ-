from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=40)
    cotent = models.TextField()
    create_at = models.DateField()


    ########함수함수함수 str함수는 화면에 보이는걸 할 때 쓴다.########
    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f"/blog/{self.pk}/"


class comment(models.Model):
    #댓글에 들어갈 것 내용, 작성날짜
    cont = models.TextField()
    create = models.DateField()
    
    def __str__(self):
        return f'{self.cont}'