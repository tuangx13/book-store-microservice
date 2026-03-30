# 🔐 Tài Khoản Hệ Thống - Tổng Hợp Đầy Đủ

> Tài khoản để đăng nhập vào các dịch vụ khác nhau trong hệ thống Bookstore Microservice

---

## 📋 Mục lục

1. [Django Admin (API Gateway)](#-django-admin-api-gateway)
2. [Auth Service](#-auth-service)
3. [Customer Service](#-customer-service)
4. [Database Admin Panels](#-database-admin-panels)
5. [Quick Reference](#-quick-reference)
6. [Test Commands](#-test-commands)

---

## 🔑 Django Admin (API Gateway)

**Port:** 8000  
**URL:** http://localhost:8000/admin/

### Admin Account
| Trường | Giá trị |
|-------|--------|
| **Username** | admin |
| **Password** | admin123 |
| **Email** | admin@bookstore.com |
| **Role** | Superuser (Full Access) |

### Staff Account
| Trường | Giá trị |
|-------|--------|
| **Username** | staff |
| **Password** | staff123 |
| **Email** | staff@bookstore.com |
| **Role** | Staff (Limited Access) |

**Quyền hạn:**
- ✅ Xem/Chỉnh sửa tất cả dữ liệu
- ✅ Quản lý sách, khách hàng, đơn hàng
- ✅ Quản lý danh mục, thanh toán, vận chuyển
- ✅ Quản lý nhân viên

---

## 👑 Auth Service

**Port:** 8012  
**URL:** http://localhost:8012/auth/login/  
**Database:** PostgreSQL (auth_db)

### Admin User
| Trường | Giá trị |
|-------|--------|
| **Email** | admin@bookstore.com |
| **Password** | admin123 |
| **Role** | admin |
| **Status** | Active |

### Staff User
| Trường | Giá trị |
|-------|--------|
| **Email** | staff@bookstore.com |
| **Password** | staff123 |
| **Role** | staff |
| **Status** | Active |

### Customer Users (Auth Service)
| Email | Password | Role | Mục đích |
|-------|----------|------|---------|
| user1@bookstore.com | user123 | customer | Customer 1 |
| user2@bookstore.com | user123 | customer | Customer 2 |
| user3@bookstore.com | user123 | customer | Customer 3 |

### Service Integration Account
| Trường | Giá trị |
|-------|--------|
| **Email** | service@bookstore.com |
| **Password** | service123 |
| **Role** | service |
| **Purpose** | Internal Integration |

**Login via API:**
```bash
curl -X POST http://localhost:8012/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@bookstore.com",
    "password": "admin123"
  }'
```

---

## 👥 Customer Service

**Port:** 8001  
**URL:** http://localhost:8001/  
**Database:** MySQL (bookstore_mysql)

### Sample Customers

#### 1️⃣ Nguyen Van A
| Trường | Giá trị |
|-------|--------|
| **Email** | nguyenvana@example.com |
| **Password** | password123 |
| **Name** | Nguyen Van A |
| **Job** | Software Engineer |
| **Company** | Tech Corp |
| **Industry** | IT |
| **Addresses** | 2 addresses in Ho Chi Minh |

**Login:**
```bash
curl -X POST http://localhost:8001/customers/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "nguyenvana@example.com",
    "password": "password123"
  }'
```

#### 2️⃣ Tran Thi B
| Trường | Giá trị |
|-------|--------|
| **Email** | tranthib@example.com |
| **Password** | password123 |
| **Name** | Tran Thi B |
| **Job** | Product Manager |
| **Company** | Tech Corp |
| **Industry** | Business |
| **Addresses** | 1 address in Hanoi |

#### 3️⃣ Hoang Duc C
| Trường | Giá trị |
|-------|--------|
| **Email** | hoangducc@example.com |
| **Password** | password123 |
| **Name** | Hoang Duc C |
| **Job** | Designer |
| **Company** | Design Studio |
| **Industry** | Creative |
| **Addresses** | 1 address in Da Nang |

#### 4️⃣ Pham Thi D
| Trường | Giá trị |
|-------|--------|
| **Email** | phamthid@example.com |
| **Password** | password123 |
| **Name** | Pham Thi D |
| **Job** | Doctor |
| **Company** | Hospital |
| **Industry** | Healthcare |
| **Addresses** | 1 address in Ho Chi Minh |

#### 5️⃣ Le Van E
| Trường | Giá trị |
|-------|--------|
| **Email** | levane@example.com |
| **Password** | password123 |
| **Name** | Le Van E |
| **Job** | Student |
| **Company** | University |
| **Industry** | Education |
| **Addresses** | 1 address in Hanoi |

---

## 🗄️ Database Admin Panels

### pgAdmin (PostgreSQL)

| Trường | Giá trị |
|-------|--------|
| **URL** | http://localhost:8081 |
| **Email** | admin@admin.com |
| **Password** | admin123 |
| **Port** | 5433 (host) |
| **Host** | postgres (inside network) |

**Databases:**
- `auth_db` (auth-service)
- `bookstore_postgres` (api-gateway, cart-service)
- `catalog_db` (catalog-service)
- `order_db` (order-service)
- `pay_db` (pay-service)
- `ship_db` (ship-service)
- `staff_db` (staff-service)
- `manager_db` (manager-service)
- `comment_db` (comment-rate-service)
- `clothe_db` (clothe-service)
- `recommender_db` (recommender-ai-service)

### phpMyAdmin (MySQL)

| Trường | Giá trị |
|-------|--------|
| **URL** | http://localhost:8080 |
| **Username** | bookstore_user |
| **Password** | bookstore_pass |
| **Port** | 3307 (host) |
| **Host** | mysql (inside network) |

**Database:**
- `bookstore_mysql` (book-service, customer-service)

### RabbitMQ Management

| Trường | Giá trị |
|-------|--------|
| **URL** | http://localhost:15672 |
| **Username** | guest |
| **Password** | guest |
| **Port** | 15672 |

---

## 📊 Quick Reference

### Admin/Staff Login URLs
```
Django Admin:     http://localhost:8000/admin/
Auth API:         http://localhost:8012/auth/login/
Customer API:     http://localhost:8001/customers/login/
```

### All Admin/Staff Credentials

| Account | Email | Username | Password | Service |
|---------|-------|----------|----------|---------|
| Admin | admin@bookstore.com | admin | admin123 | Django + Auth Service |
| Staff | staff@bookstore.com | staff | staff123 | Django + Auth Service |

### Sample Customer Credentials (for testing)

| # | Email | Password | Name |
|----|-------|----------|------|
| 1 | nguyenvana@example.com | password123 | Nguyen Van A |
| 2 | tranthib@example.com | password123 | Tran Thi B |
| 3 | hoangducc@example.com | password123 | Hoang Duc C |
| 4 | phamthid@example.com | password123 | Pham Thi D |
| 5 | levane@example.com | password123 | Le Van E |

### Service Integration

| Email | Password | Role | Purpose |
|-------|----------|------|---------|
| service@bookstore.com | service123 | service | Internal APIs |

### Database Admin Panels

| Tool | URL | User | Password |
|------|-----|------|----------|
| pgAdmin | http://localhost:8081 | admin@admin.com | admin123 |
| phpMyAdmin | http://localhost:8080 | bookstore_user | bookstore_pass |
| RabbitMQ | http://localhost:15672 | guest | guest |

---

## 🧪 Test Commands

### Test Django Admin Login
```bash
curl -X POST http://localhost:8000/admin/login/ \
  -c cookies.txt \
  -d "username=admin&password=admin123"
```

### Test Auth Service - Admin Login
```bash
curl -X POST http://localhost:8012/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@bookstore.com",
    "password": "admin123"
  }'
```

### Test Auth Service - Staff Login
```bash
curl -X POST http://localhost:8012/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "staff@bookstore.com",
    "password": "staff123"
  }'
```

### Test Customer Login
```bash
curl -X POST http://localhost:8001/customers/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "nguyenvana@example.com",
    "password": "password123"
  }'
```

### Get Access Token (Auth Service)
```bash
# Get token
TOKEN=$(curl -s -X POST http://localhost:8012/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@bookstore.com",
    "password": "admin123"
  }' | jq -r '.access')

echo "Token: $TOKEN"

# Use token in API calls
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:8012/auth/validate-token/
```

### Check All Seeded Customers
```bash
curl http://localhost:8001/customers/ | python -m json.tool
```

### Verify Auth Users
```bash
# From Docker
docker-compose exec auth-service python manage.py shell -c \
  "from app.models import AuthUser; \
   [print(f'{u.email} - {u.role}') for u in AuthUser.objects.all()]"
```

---

## 🔄 Re-seed Accounts

Nếu cần tạo lại tất cả tài khoản:

### Option 1: Run All Seeds
```bash
cd seed/
./seed-all.sh
```

### Option 2: Seed Individual Services
```bash
# Auth Service
docker-compose exec auth-service python manage.py seed_auth

# Customer Service
docker-compose exec customer-service python manage.py seed_customers

# Other services
docker-compose exec book-service python manage.py seed_books
docker-compose exec catalog-service python manage.py seed_catalog
docker-compose exec clothe-service python manage.py seed_clothes
```

### Option 3: Create Django Admin Users Manually
```bash
# Admin
docker-compose exec -e DJANGO_SUPERUSER_PASSWORD=admin123 \
  api-gateway python manage.py createsuperuser \
  --noinput --username admin --email admin@bookstore.com

# Staff
docker-compose exec -e DJANGO_SUPERUSER_PASSWORD=staff123 \
  api-gateway python manage.py createsuperuser \
  --noinput --username staff --email staff@bookstore.com
```

---

## 📝 Chú ý quan trọng

⚠️ **Password Policy:**
- Admin: `admin123` (8 characters, mix of letters and numbers)
- Staff: `staff123` (8 characters, mix of letters and numbers)
- Customers: `password123` (11 characters)
- Service: `service123` (10 characters)

⚠️ **Account Types:**
- **Django Users**: Dùng cho Django `/admin/` interface
- **Auth Service**: Dùng cho API endpoints via JWT tokens
- **Customer Users**: Dùng cho khách hàng login storefront

⚠️ **Security Notes:**
- Đây là Development credentials, không dùng cho Production
- Tất cả passwords lưu trong plain text trong seed files
- Thay đổi passwords trước khi deploy lên production

---

**Last Updated:** 2026-03-30  
**Status:** ✅ All accounts tested and working
