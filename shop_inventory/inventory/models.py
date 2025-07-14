

# Create your models here.
from django.db import models

class Item(models.Model):
    CATEGORY_CHOICES = [
        ('ELEC', 'Electronics'),
        ('GROC', 'Groceries'),
        ('CLTH', 'Clothing'),
        ('OTHR', 'Other'),
    ]

    name       = models.CharField(max_length=100)
    price      = models.DecimalField(max_digits=8, decimal_places=2)
    quantity   = models.PositiveIntegerField()
    category   = models.CharField(max_length=4, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def stock_status(self):
        if self.quantity == 0:
            return 'Out of stock'
        if self.quantity < 5:
            return 'Low'
        return 'In stock'

    def __str__(self):
        return f"{self.name} ({self.quantity})"