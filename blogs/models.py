from django.db import models
from ckeditor.fields import RichTextField
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    email = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self) -> str:
        return super.__str__(self.name)

class Popular(models.Model):
    ranking = models.IntegerField()
    topic = models.CharField(max_length=50)
    heading = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    postDate = models.DateField(auto_now_add=True)
    cover = models.ImageField(upload_to='new_blog', null=True)
    content = RichTextField()

class Regular_blogs(models.Model):
    topic = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = RichTextField()
    postDate = models.DateField(auto_now_add=True, null=True)
    cover = models.ImageField(upload_to='new_blog')