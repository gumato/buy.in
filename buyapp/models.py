from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300)

class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products')
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return self.name

