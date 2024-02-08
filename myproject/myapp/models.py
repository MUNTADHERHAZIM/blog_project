from django.db import models
from django.contrib.auth.models import User 
from ckeditor.fields import RichTextField  # Import the missing module
from ckeditor_uploader.fields import RichTextUploadingField
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    body =  RichTextUploadingField()
    
    def __str__(self):
        return self.title + '|' + str(self.author)


class summary(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    body =  RichTextUploadingField()
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title 
    

    