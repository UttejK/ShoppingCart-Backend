from django.core.management.base import BaseCommand
from api.models import Product, Cart, Purchase
from django.db import connection


class Command(BaseCommand):
    help = 'Remove all entries from the Product table and reset the primary key sequence.'

    def handle(self, *args, **kwargs):
        # Delete all entries from the Product table
        Product.objects.all().delete()
        Cart.objects.all().delete()
        Purchase.objects.all().delete()

        # Reset the primary key sequence for Product table to start from 1
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='api_product';")

        self.stdout.write(self.style.SUCCESS(
            'All entries from the Product table have been removed, and primary key sequence has been reset.'))
