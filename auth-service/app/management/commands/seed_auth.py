from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from app.models import AuthUser

class Command(BaseCommand):
    help = 'Seed database with sample auth users'

    def handle(self, *args, **options):
        users_data = [
            {"email": "admin@bookstore.com", "password": "admin123", "role": "admin"},
            {"email": "staff@bookstore.com", "password": "staff123", "role": "staff"},
            {"email": "user1@bookstore.com", "password": "user123", "role": "customer"},
            {"email": "user2@bookstore.com", "password": "user123", "role": "customer"},
            {"email": "user3@bookstore.com", "password": "user123", "role": "customer"},
            {"email": "service@bookstore.com", "password": "service123", "role": "service"},
        ]

        created_count = 0
        for user_data in users_data:
            user, created = AuthUser.objects.get_or_create(
                email=user_data["email"],
                defaults={
                    "password": make_password(user_data["password"]),
                    "role": user_data["role"],
                    "is_active": True,
                }
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f'✓ Successfully seeded {created_count} auth users')
        )
