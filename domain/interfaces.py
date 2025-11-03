from abc import ABC, abstractmethod
from entities import Order, Customer

class IOrderRepository(ABC):
    @abstractmethod
    def check_stock(self, product_id: str, quantity: int) -> bool:
        pass

    @abstractmethod
    def save_order(self, order: Order) -> None:
        pass

    @abstractmethod
    def get_customer(self, customer_id: str) -> Customer:
        pass

class INotificationSender(ABC):
    @abstractmethod
    def send_confirmation(self, email: str, order_id: str) -> None:
        pass