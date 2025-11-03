import sqlite3
from domain.entities import Order, Customer
from domain.interfaces import IOrderRepository

class SqliteOrderRepository(IOrderRepository):
    def __init__(self, db_path: str = "shopflow.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    stock INTEGER
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                    id TEXT PRIMARY KEY,
                    email TEXT
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS orders (
                    id TEXT PRIMARY KEY,
                    customer_id TEXT
                )
            """)
            # Insert sample data
            conn.execute("INSERT OR IGNORE INTO products VALUES ('p1', 'Laptop', 10)")
            conn.execute("INSERT OR IGNORE INTO customers VALUES ('cust_123', 'user@example.com')")

    def check_stock(self, product_id: str, quantity: int) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT stock FROM products WHERE id = ?", (product_id,))
            row = cursor.fetchone()
            return row[0] >= quantity if row else False

    def save_order(self, order: Order) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO orders (id, customer_id) VALUES (?, ?)",
                (order.id, order.customer_id)
            )

    def get_customer(self, customer_id: str) -> Customer:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, email FROM customers WHERE id = ?", (customer_id,))
            row = cursor.fetchone()
            if not row:
                raise ValueError(f"Customer {customer_id} not found")
            return Customer(id=row[0], email=row[1])