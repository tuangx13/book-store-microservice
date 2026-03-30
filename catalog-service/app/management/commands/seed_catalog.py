from django.core.management.base import BaseCommand
from app.models import Category, BookCatalog

class Command(BaseCommand):
    help = 'Seed database with sample categories and book mappings'

    def handle(self, *args, **options):
        categories_data = [
            {"name": "Technology", "description": "Programming and tech books"},
            {"name": "Business", "description": "Business and management books"},
            {"name": "Science", "description": "Science and research books"},
            {"name": "Education", "description": "Educational materials"},
            {"name": "Self-Help", "description": "Personal development books"},
        ]

        created_categories = 0
        for cat_data in categories_data:
            cat, created = Category.objects.get_or_create(
                name=cat_data["name"],
                defaults={"description": cat_data["description"]}
            )
            if created:
                created_categories += 1

        # Map books to categories (book_id: 1 to 8 from seed_books)
        mappings = [
            (1, "Technology"),  # Python Programming
            (1, "Education"),   # Python Programming
            (2, "Technology"),  # Django for Beginners
            (3, "Technology"),  # Clean Code
            (3, "Business"),    # Clean Code
            (4, "Technology"),  # The Pragmatic Programmer
            (5, "Technology"),  # Design Patterns
            (6, "Science"),     # Algorithms
            (7, "Science"),     # Machine Learning Basics
            (8, "Technology"),  # Web Development with Flask
        ]

        created_mappings = 0
        for book_id, category_name in mappings:
            try:
                category = Category.objects.get(name=category_name)
                mapping, created = BookCatalog.objects.get_or_create(
                    book_id=book_id,
                    category=category
                )
                if created:
                    created_mappings += 1
            except Category.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Category {category_name} not found'))

        self.stdout.write(
            self.style.SUCCESS(
                f'✓ Successfully seeded {created_categories} categories and {created_mappings} mappings'
            )
        )
