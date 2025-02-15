from django.db import models
from django.contrib.auth.models import User

class Gallery(models.Model):
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    title3 = models.CharField(max_length=255)
    feedimage = models.ImageField(upload_to='gallery_images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gallery_item = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.gallery_item.title1} x {self.quantity}"

    def total_price(self):
        return self.gallery_item.price * self.quantity  # Assuming each product has a 'price' field  

