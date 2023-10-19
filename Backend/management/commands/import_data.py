# Backend/management/commands/import_data.py
import csv
from django.core.management.base import BaseCommand
from Backend.models import Product

class Command(BaseCommand):
    help = 'Import data from CSV file into the database'

    def handle(self, *args, **kwargs):
        with open('D:/Downloads/MasterDB_rows.csv', 'r') as csvfile:  # Use forward slash (/) or double backslashes (\\) in the path
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip header row if it exists
            for row in csvreader:
                # Extract values from the row
                name = row[0]  # Text field
                total_available = int(row[1])  # Convert to integer
                price = float(row[2])  # Convert to float
                image_url = row[3]  # Text field (assuming it's a URL)
                description = row[4]  # Text field
                category = row[5]  # Text field

                # Create or update the database record
                _, created = Product.objects.update_or_create(
                    name=name,
                    defaults={
                        'total_available': total_available,
                        'price': price,
                        'image_url': image_url,
                        'description': description,
                        'category': category
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added {name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'{name} already exists'))
