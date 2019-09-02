from django.db import models

# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    publish = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    comment = models.TextField(max_length=255)
    publish = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.article.title


