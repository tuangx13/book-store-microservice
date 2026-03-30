# ✨ Quick Start Guide - English

All microservices are running with complete sample data!

## 📊 Current Status

```
✅ 14 Services Running
✅ All Databases Initialized
✅ Sample Data Seeded:
   - 8 Books
   - 5 Customers
   - 10 Clothes
   - 5 Categories
   - 11 Job Types
   - 6 Auth Users
```

## 🚀 Test Commands

### Verify All Data
```bash
cd seed/
./verify-seeds.sh
```

### Test Books (Port 8002)
```bash
curl http://localhost:8002/books/ | python -m json.tool
```

### Test Customers (Port 8001)
```bash
curl http://localhost:8001/customers/ | python -m json.tool
```

### Test Clothes (Port 8013)
```bash
curl http://localhost:8013/clothes/ | python -m json.tool
```

### Test Login
```bash
curl -X POST http://localhost:8001/customers/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "nguyenvana@example.com",
    "password": "password123"
  }'
```

## 🔐 Test Credentials

**Admin:**
- Email: admin@bookstore.com
- Password: admin123

**Customer Sample:**
- Email: nguyenvana@example.com
- Password: password123
- Job: Software Engineer

**Generic Users:**
- Email: user1@bookstore.com, user2@bookstore.com, user3@bookstore.com
- Password: user123

## 🛠️ Admin Panels

| Tool | URL | Login |
|------|-----|-------|
| pgAdmin | http://localhost:8081 | admin@admin.com / admin123 |
| phpMyAdmin | http://localhost:8080 | bookstore_user / bookstore_pass |
| RabbitMQ | http://localhost:15672 | guest / guest |

## 📚 API Endpoints (No /api/ prefix!)

**Books:**
```bash
curl http://localhost:8002/books/           # List
curl http://localhost:8002/books/1/         # Get one
curl -X POST http://localhost:8002/books/ \ # Create
  -H "Content-Type: application/json" \
  -d '{"title":"Book","author":"Author","price":29.99,"stock":50}'
```

**Customers:**
```bash
curl http://localhost:8001/customers/       # List
curl http://localhost:8001/customers/1/     # Get one
curl http://localhost:8001/jobs/            # List jobs
```

**Clothes:**
```bash
curl http://localhost:8013/clothes/         # List
curl http://localhost:8013/clothes/1/       # Get one
```

**Categories:**
```bash
curl http://localhost:8007/categories/      # List
curl http://localhost:8007/book-catalogs/   # List mappings
```

## 📖 Full Documentation

- **seed/SEEDING_GUIDE.md** - Complete API documentation
- **seed/DATA_READY.md** - Quick reference
- **seed/verify-seeds.sh** - Data verification script

## 🔄 Re-seed Data

```bash
cd seed/
./seed-all.sh
```

## 🐳 Docker Commands

```bash
# Check status
docker-compose ps

# View logs
docker-compose logs -f [service-name]

# Restart services
docker-compose restart

# Rebuild and start
docker-compose up --build

# Stop everything
docker-compose down
```

## ✨ Key Features

✅ All services running with sample data
✅ PostgreSQL + MySQL databases
✅ RabbitMQ message queue
✅ Admin panels included
✅ Easy verification script
✅ Idempotent seed scripts
✅ Complete API documentation

## 🎯 Next Steps

1. Run `verify-seeds.sh` to check data
2. Test APIs with curl commands above
3. Login to admin panels
4. Explore the microservices
5. Create test orders and transactions

---

**Ready to test!** 🚀

For detailed API documentation, see **seed/SEEDING_GUIDE.md**
