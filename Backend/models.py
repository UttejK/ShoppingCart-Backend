from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-generated primary key
    name = models.CharField(max_length=255)
    total_available = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()
    description = models.TextField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name
