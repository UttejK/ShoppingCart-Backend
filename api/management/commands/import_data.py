import csv
from django.core.management.base import BaseCommand
from api.models import Product


class Command(BaseCommand):
    help = 'Import data from CSV file into the database'

    def handle(self, *args, **kwargs):
        with open(r'D:\Projects\web\ReactJS\djangot2\MasterDB_rows.csv',
                  'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
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
