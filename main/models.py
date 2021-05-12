from django.db import models

# Create your models here.

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:5] ## 적절량 짜르기 


# 클래스 머델 생성, migrate해주기, superuser만들기, 블로그 쓰기, 블로그 제목 뜨게 만들기, 
