from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_id = models.IntegerField()
    product_price = models.IntegerField()
    product_desc = models.CharField(max_length=200)

    def __str__(self):
        return self.product_name   #this function used show admin panel what product name instead of obeject 1 and object 2

class Order(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_num = models.IntegerField()
    order_address = models.CharField(max_length=500)
    order_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.order_address  #this function used show admin panel what product name instead of obeject 1 and object 2
