from django.db import models


class BlogPost(models.Model):
    name        =models.CharField(max_length=120)
    title       =models.CharField(max_length=200)
    content     =models.TextField()

    def __str__(self):
        return self.name


