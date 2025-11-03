from application.use_cases import PlaceOrderUseCase
from infrastructure.repositories.sqlite_repo import SqliteOrderRepository
from infrastructure.notifications.email_sender import EmailSender

if __name__ == "__main__":
    # Wire dependencies at the boundary
    repo = SqliteOrderRepository()
    notifier = EmailSender()
    use_case = PlaceOrderUseCase(repo, notifier)

    try:
        order_id = use_case.execute("cust_123", [{"product_id": "p1", "quantity": 1}])
        print(f"Order placed successfully: {order_id}")
    except Exception as e:
        print(f"Error: {e}")