from domain.interfaces import INotificationSender

class SmsSender(INotificationSender):
    def send_confirmation(self, email: str, order_id: str) -> None:
        print(f"[SMS] Sent confirmation for order {order_id}")