from django.db import models
from django.db.models import ImageField

# Create your models here.
class Product(models.Model):  
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='./static/Image/uploads')

   
    class Meta:  
        db_table = "product"


class Users(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    isAdmin = models.BooleanField(default=False)

    class Meta: 
        db_table = "users"


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='./static/Image/uploads/cart_images/')

    class Meta:
        db_table = "list_cart_products"
        
    def subtotal(self):
        return self.product.price * self.quantity
    
class Team(models.Model):  
    name = models.CharField(max_length=255)
    StudentId = models.CharField(max_length=255)
    social = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='./static/Image/uploads/team')

    class Meta:  
        db_table = "team"


class Contact(models.Model):
    username = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=255)
    message = models.TextField()

    class Meta: 
        db_table = "contact"


