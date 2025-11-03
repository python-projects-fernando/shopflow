from domain.entities import Order, OrderItem
from domain.interfaces import IOrderRepository, INotificationSender
import uuid

class PlaceOrderUseCase:
    def __init__(
        self,
        order_repo: IOrderRepository,
        notifier: INotificationSender
    ):
        self.order_repo = order_repo
        self.notifier = notifier

    def execute(self, customer_id: str, items: list[dict]) -> str:
        # Validate stock for each item
        for item in items:
            if not self.order_repo.check_stock(item["product_id"], item["quantity"]):
                raise ValueError("Insufficient stock")

        # Create order with proper entities
        order_id = str(uuid.uuid4())
        order_items = [OrderItem(item["product_id"], item["quantity"]) for item in items]
        order = Order(order_id, customer_id, order_items)
        self.order_repo.save_order(order)

        # Notify using customer email from separate aggregate
        customer = self.order_repo.get_customer(customer_id)
        self.notifier.send_confirmation(customer.email, order_id)

        return order_id