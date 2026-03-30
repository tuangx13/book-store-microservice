# 🌱 Database Seeding Guide

✅ **All data has been successfully created!**

## ✅ Data Created

### 📚 Book Service (Port 8002)
**8 Books:**
- Python Programming - Guido van Rossum ($29.99)
- Django for Beginners - William Vincent ($39.99)
- Clean Code - Robert Martin ($49.99)
- The Pragmatic Programmer - David Thomas ($44.99)
- Design Patterns - Gang of Four ($59.99)
- Algorithms - Robert Sedgewick ($69.99)
- Machine Learning Basics - Andrew Ng ($54.99)
- Web Development with Flask - Miguel Grinberg ($42.99)

**API Endpoints:**
```bash
# List all books
curl http://localhost:8002/books/

# Get a specific book
curl http://localhost:8002/books/1/

# Create new book
curl -X POST http://localhost:8002/books/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New Book",
    "author": "Author Name",
    "price": 29.99,
    "stock": 50
  }'

# Reduce stock
curl -X POST http://localhost:8002/books/1/reduce-stock/ \
  -H "Content-Type: application/json" \
  -d '{"quantity": 5}'

# Restore stock
curl -X POST http://localhost:8002/books/1/restore-stock/ \
  -H "Content-Type: application/json" \
  -d '{"quantity": 5}'
```

### 📑 Catalog Service (Port 8007)
**5 Categories:**
- Technology
- Business
- Science
- Education
- Self-Help

**10 Book-to-Category Mappings**

**API Endpoints:**
```bash
# List categories
curl http://localhost:8007/categories/

# Get a specific category
curl http://localhost:8007/categories/1/

# List book mappings
curl http://localhost:8007/book-catalogs/

# Get mappings for a specific book
curl "http://localhost:8007/book-catalogs/?book_id=1"

# Create new mapping
curl -X POST http://localhost:8007/book-catalogs/ \
  -H "Content-Type: application/json" \
  -d '{
    "book_id": 1,
    "category": 1
  }'
```

### 👥 Customer Service (Port 8001)
**5 Customers with Addresses:**

1. **Nguyen Van A** - nguyenvana@example.com (Software Engineer)
   - Address: 123 Le Loi, Ho Chi Minh (default)
   - Address: 456 Tran Hung Dao, Ho Chi Minh

2. **Tran Thi B** - tranthib@example.com (Product Manager)
   - Address: 789 Nguyen Hue, Hanoi (default)

3. **Hoang Duc C** - hoangducc@example.com (Designer)
   - Address: 321 Hai Ba Trung, Da Nang (default)

4. **Pham Thi D** - phamthid@example.com (Doctor)
   - Address: 654 Pasteur, Ho Chi Minh (default)

5. **Le Van E** - levane@example.com (Student)
   - Address: 987 Dinh Tien Hoang, Hanoi (default)

**All passwords:** `password123`

**7 Job Types:**
- Software Engineer (IT, Tech Corp)
- Product Manager (Business, Tech Corp)
- Designer (Creative, Design Studio)
- Doctor (Healthcare, Hospital)
- Teacher (Education, School)
- Sales Executive (Retail, Retail Store)
- Student (Education, University)

**API Endpoints:**
```bash
# List customers
curl http://localhost:8001/customers/

# Get a specific customer
curl http://localhost:8001/customers/1/

# List job types
curl http://localhost:8001/jobs/

# Create new customer
curl -X POST http://localhost:8001/customers/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "New Customer",
    "email": "newcust@example.com",
    "job_id": 1
  }'

# Update customer
curl -X PATCH http://localhost:8001/customers/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Name",
    "job_id": 2
  }'

# Customer login
curl -X POST http://localhost:8001/customers/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "nguyenvana@example.com",
    "password": "password123"
  }'
```

### 👗 Clothe Service (Port 8013)
**10 Clothing Items:**
- T-Shirt (Cotton, $19.99, 100 in stock)
- Jeans (Denim, $49.99, 50 in stock)
- Jacket (Polyester, $79.99, 30 in stock)
- Shirt (Cotton, $39.99, 60 in stock)
- Dress (Silk, $89.99, 25 in stock)
- Sweater (Wool, $59.99, 40 in stock)
- Shorts (Cotton, $29.99, 70 in stock)
- Skirt (Cotton, $44.99, 35 in stock)
- Blazer (Polyester, $99.99, 20 in stock)
- Hoodie (Cotton, $54.99, 45 in stock)

**API Endpoints:**
```bash
# List clothes
curl http://localhost:8013/clothes/

# Get specific clothing item
curl http://localhost:8013/clothes/1/

# Create new clothing item
curl -X POST http://localhost:8013/clothes/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "New Item",
    "material": "Leather",
    "price": 199.99,
    "stock": 15
  }'
```

### 🔐 Auth Service (Port 8012)
**6 Authentication Users:**

| Email | Password | Role | Purpose |
|-------|----------|------|---------|
| admin@bookstore.com | admin123 | admin | Administrator |
| staff@bookstore.com | staff123 | staff | Staff Member |
| user1@bookstore.com | user123 | customer | Customer 1 |
| user2@bookstore.com | user123 | customer | Customer 2 |
| user3@bookstore.com | user123 | customer | Customer 3 |
| service@bookstore.com | service123 | service | Integration |

## 🔄 Re-run Seeds

If you need to populate the data again (after clearing the database):

```bash
# Run all seeds
./seed-all.sh

# Or individually:
docker exec django-ecommerce-microservices-book-service-1 python manage.py seed_books
docker exec django-ecommerce-microservices-catalog-service-1 python manage.py seed_catalog
docker exec django-ecommerce-microservices-customer-service-1 python manage.py seed_customers
docker exec django-ecommerce-microservices-clothe-service-1 python manage.py seed_clothes
docker exec django-ecommerce-microservices-auth-service-1 python manage.py seed_auth
```

## 🗄️ Access Data via Admin Panels

### pgAdmin (PostgreSQL) - Port 8081
- **URL:** http://localhost:8081
- **Email:** admin@admin.com
- **Password:** admin123

**Available Databases:**
- bookstore_postgres (api-gateway, cart-service)
- auth_db (auth-service)
- catalog_db (catalog-service)
- order_db (order-service)
- pay_db (pay-service)
- ship_db (ship-service)
- staff_db (staff-service)
- manager_db (manager-service)
- comment_db (comment-rate-service)
- clothe_db (clothe-service)
- recommender_db (recommender-ai-service)

### phpMyAdmin (MySQL) - Port 8080
- **URL:** http://localhost:8080
- **User:** bookstore_user
- **Password:** bookstore_pass

**Database:**
- bookstore_mysql (book-service, customer-service)

### RabbitMQ Management - Port 15672
- **URL:** http://localhost:15672
- **User:** guest
- **Password:** guest

## 🧪 Complete Test Examples

### 1. Check Books
```bash
curl http://localhost:8002/books/ | python -m json.tool
```

### 2. List Categories
```bash
curl http://localhost:8007/categories/ | python -m json.tool
```

### 3. Check Customers
```bash
curl http://localhost:8001/customers/ | python -m json.tool
```

### 4. Customer Login
```bash
curl -X POST http://localhost:8001/customers/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "nguyenvana@example.com",
    "password": "password123"
  }' | python -m json.tool
```

### 5. Check Clothes
```bash
curl http://localhost:8013/clothes/ | python -m json.tool
```

### 6. Count Total Records
```bash
echo "📚 Books: $(curl -s http://localhost:8002/books/ | python -m json.tool | grep -c '\"id\"')"
echo "👥 Customers: $(curl -s http://localhost:8001/customers/ | python -m json.tool | grep -c '\"id\"')"
echo "👗 Clothes: $(curl -s http://localhost:8013/clothes/ | python -m json.tool | grep -c '\"id\"')"
echo "📑 Categories: $(curl -s http://localhost:8007/categories/ | python -m json.tool | grep -c '\"id\"')"
```

## 📝 Seed Script Structure

All seed scripts are located in:
```
book-service/app/management/commands/seed_books.py
catalog-service/app/management/commands/seed_catalog.py
customer-service/app/management/commands/seed_customers.py
clothe-service/app/management/commands/seed_clothes.py
auth-service/app/management/commands/seed_auth.py
```

The scripts are **idempotent** - you can run them multiple times without creating duplicates!

## 🚀 Next Steps

1. ✅ Data successfully created!
2. 📝 Test APIs with curl
3. 🛒 Integrate data with order/cart flow
4. 📊 Create more data as needed
5. 🔄 Consider automating seeds in docker-compose

---

**Created on:** 2026-03-30
**Status:** ✅ All data successfully seeded
