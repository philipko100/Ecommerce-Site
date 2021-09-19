from decimal import Decimal

from django.conf import settings
from django.db import models
from store.models import Product


class InventoryItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='inventory_user')
    product = models.ForeignKey(Product,
                                related_name='inventory_items',
                                on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
