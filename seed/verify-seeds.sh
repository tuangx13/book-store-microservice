#!/bin/bash

# Verification script for seeded data

echo "🔍 Verifying Seeded Data"
echo "=================================="
echo

# Function to count items in JSON array
count_json_items() {
    echo "$1" | python -m json.tool 2>/dev/null | grep -c '"id"'
}

# 1. Books
echo "📚 Book Service (http://localhost:8002)"
books_response=$(curl -s http://localhost:8002/books/)
books_count=$(count_json_items "$books_response")
echo "   ✓ Books: $books_count"
echo "   Sample: $(echo "$books_response" | python -m json.tool 2>/dev/null | grep '"title"' | head -1)"
echo

# 2. Customers
echo "👥 Customer Service (http://localhost:8001)"
customers_response=$(curl -s http://localhost:8001/customers/)
customers_count=$(count_json_items "$customers_response")
echo "   ✓ Customers: $customers_count"
echo "   Sample: $(echo "$customers_response" | python -m json.tool 2>/dev/null | grep '"name"' | head -1)"
echo

# 3. Categories
echo "📑 Catalog Service (http://localhost:8007)"
categories_response=$(curl -s http://localhost:8007/categories/)
categories_count=$(count_json_items "$categories_response")
echo "   ✓ Categories: $categories_count"
echo "   Sample: $(echo "$categories_response" | python -m json.tool 2>/dev/null | grep '"name"' | head -1)"
echo

# 4. Book Catalogs
bookcatalogs_response=$(curl -s http://localhost:8007/book-catalogs/)
bookcatalogs_count=$(count_json_items "$bookcatalogs_response")
echo "   ✓ Book Catalogs: $bookcatalogs_count"
echo

# 5. Clothes
echo "👗 Clothe Service (http://localhost:8013)"
clothes_response=$(curl -s http://localhost:8013/clothes/)
clothes_count=$(count_json_items "$clothes_response")
echo "   ✓ Clothes: $clothes_count"
echo "   Sample: $(echo "$clothes_response" | python -m json.tool 2>/dev/null | grep '"name"' | head -1)"
echo

# 6. Jobs
echo "💼 Jobs (http://localhost:8001/jobs/)"
jobs_response=$(curl -s http://localhost:8001/jobs/)
jobs_count=$(count_json_items "$jobs_response")
echo "   ✓ Jobs: $jobs_count"
echo

# Summary
echo "=================================="
echo "📊 Summary:"
echo "   - Books: $books_count"
echo "   - Customers: $customers_count"
echo "   - Categories: $categories_count"
echo "   - Book Catalogs: $bookcatalogs_count"
echo "   - Clothes: $clothes_count"
echo "   - Jobs: $jobs_count"
echo

# Test customer login
echo "🔐 Testing Customer Login:"
login_response=$(curl -s -X POST http://localhost:8001/customers/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "nguyenvana@example.com",
    "password": "password123"
  }')

if echo "$login_response" | python -m json.tool 2>/dev/null | grep -q '"access"'; then
    echo "   ✓ Login successful!"
    echo "   Token received: $(echo "$login_response" | python -m json.tool 2>/dev/null | grep '"access"' | head -1)"
else
    echo "   ✗ Login failed!"
    echo "   Response: $login_response"
fi

echo
echo "✅ Verification complete!"
