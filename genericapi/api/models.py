from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    category=models.CharField(max_length=30)
    company=models.CharField(max_length=30)
    image=models.FileField(upload_to='product_image')