from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class ContactUs(models.Model):
    fullname = models.CharField(max_length=100)
    emailadd = models.CharField(max_length=100)
    phonenum = models.IntegerField()
    address = models.TextField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__(self.fullname)
    

class Popular(models.Model):
    ranking = models.IntegerField()
    topic = models.CharField(max_length=50)
    heading = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    postDate = models.DateField(auto_now_add=True)
    content = RichTextField()

class Regular(models.Model):
    topic = models.CharField(max_length=50)
    heading = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    cover = models.ImageField(upload_to="img_folder")
    postDate = models.DateField(auto_now_add=True)
    content = RichTextField()