from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

STATE_CHOICES=(
    ('Andman & Nicobar Island','Andman & Nicobar Island'),
    ('Bihar','Bihar'),
    ('Goa','Goa'),
    ('Asam','Asam'),
    ('Mijoram','Mijoram'),
    ('Andhrapradesh','Andhrapradesh'),
    ('Telangna','Telangna'),
    ('Chhatisgadh','Chhatisgadh'),
    ('maharastra','maharastra'),
    ('Jharkhand','Jharkhand'),

)
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    locality=models.CharField(max_length=50)
    city=models.CharField(max_length=40)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=50)


    def __str__(self):
        return str(self.id)



CATEGORIES_CHOICES=(
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top wear'),
    ('BW','Bottom wear'),

)   
class Product(models.Model):
    title=models.CharField(max_length=50)
    selling_price=models.IntegerField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=50)
    category=models.CharField(choices=CATEGORIES_CHOICES,max_length=3)
    product_image=models.ImageField(upload_to='productimg')



    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)  
    product=models.ForeignKey(Product,on_delete=models.CASCADE) 
    quantity=models.PositiveIntegerField(default=1)



STATUS_CHOICES=(
    ('Delevered','Acepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')

)    


class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)  
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)  
    order_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending') 





