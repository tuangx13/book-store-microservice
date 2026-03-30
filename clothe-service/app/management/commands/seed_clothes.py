from django.core.management.base import BaseCommand
from app.models import Clothe

class Command(BaseCommand):
    help = 'Seed database with sample clothes'

    def handle(self, *args, **options):
        clothes_data = [
            {"name": "T-Shirt", "material": "Cotton", "price": 19.99, "stock": 100},
            {"name": "Jeans", "material": "Denim", "price": 49.99, "stock": 50},
            {"name": "Jacket", "material": "Polyester", "price": 79.99, "stock": 30},
            {"name": "Shirt", "material": "Cotton", "price": 39.99, "stock": 60},
            {"name": "Dress", "material": "Silk", "price": 89.99, "stock": 25},
            {"name": "Sweater", "material": "Wool", "price": 59.99, "stock": 40},
            {"name": "Shorts", "material": "Cotton", "price": 29.99, "stock": 70},
            {"name": "Skirt", "material": "Cotton", "price": 44.99, "stock": 35},
            {"name": "Blazer", "material": "Polyester", "price": 99.99, "stock": 20},
            {"name": "Hoodie", "material": "Cotton", "price": 54.99, "stock": 45},
        ]

        created_count = 0
        for clothe_data in clothes_data:
            clothe, created = Clothe.objects.get_or_create(
                name=clothe_data["name"],
                material=clothe_data["material"],
                defaults={
                    "price": clothe_data["price"],
                    "stock": clothe_data["stock"],
                }
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f'✓ Successfully seeded {created_count} clothes')
        )
