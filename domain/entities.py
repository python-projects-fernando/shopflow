from dataclasses import dataclass

@dataclass
class Customer:
    id: str
    email: str

@dataclass
class OrderItem:
    product_id: str
    quantity: int

@dataclass
class Order:
    id: str
    customer_id: str
    items: list[OrderItem]