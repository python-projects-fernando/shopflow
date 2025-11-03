from unittest.mock import Mock
from application.use_cases import PlaceOrderUseCase
from domain.entities import Customer

def test_place_order_success():
    # Arrange
    mock_repo = Mock()
    mock_repo.check_stock.return_value = True
    mock_repo.get_customer.return_value = Customer(id="cust_123", email="test@example.com")

    mock_notifier = Mock()

    use_case = PlaceOrderUseCase(mock_repo, mock_notifier)

    # Act
    order_id = use_case.execute("cust_123", [{"product_id": "p1", "quantity": 1}])

    # Assert
    assert order_id is not None
    mock_repo.save_order.assert_called_once()
    mock_notifier.send_confirmation.assert_called_once_with("test@example.com", order_id)