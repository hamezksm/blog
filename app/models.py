from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    # More fields, yet to decide which ones exactly

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
