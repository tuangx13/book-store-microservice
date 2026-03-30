#!/bin/bash

# Seed all microservices with sample data

echo "🌱 Starting database seeding..."
echo

# 1. Seed Books
echo "📚 Seeding book-service..."
docker exec django-ecommerce-microservices-book-service-1 python manage.py seed_books
echo

# 2. Seed Catalog (Categories and Book Mappings)
echo "📑 Seeding catalog-service..."
docker exec django-ecommerce-microservices-catalog-service-1 python manage.py seed_catalog
echo

# 3. Seed Customers
echo "👥 Seeding customer-service..."
docker exec django-ecommerce-microservices-customer-service-1 python manage.py seed_customers
echo

# 4. Seed Clothes
echo "👗 Seeding clothe-service..."
docker exec django-ecommerce-microservices-clothe-service-1 python manage.py seed_clothes
echo

# 5. Seed Auth Users
echo "🔐 Seeding auth-service..."
docker exec django-ecommerce-microservices-auth-service-1 python manage.py seed_auth
echo

echo "✅ Database seeding completed!"
echo
echo "📍 Sample data created:"
echo "   - 8 Books in book-service"
echo "   - 5 Categories with book mappings in catalog-service"
echo "   - 5 Customers with addresses in customer-service"
echo "   - 10 Clothes in clothe-service"
echo "   - 6 Auth users in auth-service"
echo
echo "📌 Test Credentials:"
echo "   Admin:  admin@bookstore.com / admin123"
echo "   Staff:  staff@bookstore.com / staff123"
echo "   Users:  user@bookmark.com / user123 (user1, user2, user3)"
echo "   Customers: Check in customer-service (all use password: password123)"
