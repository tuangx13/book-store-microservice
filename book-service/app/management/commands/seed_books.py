from django.core.management.base import BaseCommand
from app.models import Book

class Command(BaseCommand):
    help = 'Seed database with sample books'

    def handle(self, *args, **options):
        books_data = [
            {"title": "Python Programming", "author": "Guido van Rossum", "price": 29.99, "stock": 50},
            {"title": "Django for Beginners", "author": "William Vincent", "price": 39.99, "stock": 30},
            {"title": "Clean Code", "author": "Robert Martin", "price": 49.99, "stock": 20},
            {"title": "The Pragmatic Programmer", "author": "David Thomas", "price": 44.99, "stock": 25},
            {"title": "Design Patterns", "author": "Gang of Four", "price": 59.99, "stock": 15},
            {"title": "Algorithms", "author": "Robert Sedgewick", "price": 69.99, "stock": 18},
            {"title": "Machine Learning Basics", "author": "Andrew Ng", "price": 54.99, "stock": 22},
            {"title": "Web Development with Flask", "author": "Miguel Grinberg", "price": 42.99, "stock": 28},
        ]

        created_count = 0
        for book_data in books_data:
            book, created = Book.objects.get_or_create(
                title=book_data["title"],
                defaults={
                    "author": book_data["author"],
                    "price": book_data["price"],
                    "stock": book_data["stock"],
                }
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f'✓ Successfully seeded {created_count} books')
        )
