from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    total_available = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()
    description = models.TextField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# class Purchase(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
#
#     def __str__(self):
#         return f'Purchase of {self.product.name}'

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Purchase of product ID {self.product_id} by user ID {self.user_id}'




class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Cart entry of {self.product.name}'
