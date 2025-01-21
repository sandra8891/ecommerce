from django.db import models

# Create your models here.
class Gallery(models.Model):
    feedimage=models.ImageField(upload_to='gallery_images/')
    title1=models.CharField(max_length=100)
    title2=models.CharField(max_length=100)
    title3=models.CharField(max_length=100)
