from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from app.models import Job, Customer, Address

class Command(BaseCommand):
    help = 'Seed database with sample customers, jobs, and addresses'

    def handle(self, *args, **options):
        # Create default jobs
        jobs_data = [
            {"title": "Software Engineer", "industry": "IT", "company": "Tech Corp"},
            {"title": "Product Manager", "industry": "Business", "company": "Tech Corp"},
            {"title": "Designer", "industry": "Creative", "company": "Design Studio"},
            {"title": "Doctor", "industry": "Healthcare", "company": "Hospital"},
            {"title": "Teacher", "industry": "Education", "company": "School"},
            {"title": "Sales Executive", "industry": "Retail", "company": "Retail Store"},
            {"title": "Student", "industry": "Education", "company": "University"},
        ]

        created_jobs = 0
        jobs_dict = {}
        for job_data in jobs_data:
            job, created = Job.objects.get_or_create(
                title=job_data["title"],
                defaults={
                    "industry": job_data["industry"],
                    "company": job_data["company"]
                }
            )
            if created:
                created_jobs += 1
            jobs_dict[job_data["title"]] = job

        # Create sample customers
        customers_data = [
            {
                "name": "Nguyen Van A",
                "email": "nguyenvana@example.com",
                "password": "password123",
                "job": "Software Engineer",
                "addresses": [
                    {"street": "123 Le Loi", "city": "Ho Chi Minh", "province": "HCM", "is_default": True},
                    {"street": "456 Tran Hung Dao", "city": "Ho Chi Minh", "province": "HCM", "is_default": False},
                ]
            },
            {
                "name": "Tran Thi B",
                "email": "tranthib@example.com",
                "password": "password123",
                "job": "Product Manager",
                "addresses": [
                    {"street": "789 Nguyen Hue", "city": "Hanoi", "province": "Hanoi", "is_default": True},
                ]
            },
            {
                "name": "Hoang Duc C",
                "email": "hoangducc@example.com",
                "password": "password123",
                "job": "Designer",
                "addresses": [
                    {"street": "321 Hai Ba Trung", "city": "Da Nang", "province": "Da Nang", "is_default": True},
                ]
            },
            {
                "name": "Pham Thi D",
                "email": "phamthid@example.com",
                "password": "password123",
                "job": "Doctor",
                "addresses": [
                    {"street": "654 Pasteur", "city": "Ho Chi Minh", "province": "HCM", "is_default": True},
                ]
            },
            {
                "name": "Le Van E",
                "email": "levane@example.com",
                "password": "password123",
                "job": "Student",
                "addresses": [
                    {"street": "987 Dinh Tien Hoang", "city": "Hanoi", "province": "Hanoi", "is_default": True},
                ]
            },
        ]

        created_customers = 0
        created_addresses = 0

        for cust_data in customers_data:
            job = jobs_dict.get(cust_data["job"])
            customer, created = Customer.objects.get_or_create(
                email=cust_data["email"],
                defaults={
                    "name": cust_data["name"],
                    "password": make_password(cust_data["password"]),
                    "job": job,
                }
            )
            if created:
                created_customers += 1

            # Create addresses for this customer
            for addr_data in cust_data["addresses"]:
                address, created = Address.objects.get_or_create(
                    customer=customer,
                    street=addr_data["street"],
                    city=addr_data["city"],
                    defaults={
                        "province": addr_data["province"],
                        "country": "Vietnam",
                        "is_default": addr_data["is_default"]
                    }
                )
                if created:
                    created_addresses += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'✓ Successfully seeded {created_jobs} jobs, {created_customers} customers, and {created_addresses} addresses'
            )
        )
