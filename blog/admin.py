from django.contrib import admin
###########################관리자 기능 Post여기에 추가해 줘야한다.##############
from .models import Post
from .models import comment

admin.site.register(Post)
admin.site.register(comment)


# Register your models here.
