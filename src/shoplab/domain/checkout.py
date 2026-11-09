from shoplab.domain.models import Order
from shoplab.domain.notification_bridge import send_via_bridge


def send_special_confirmation(order: Order) -> None:
    send_via_bridge(order, f"Special handling for {order.order_id}")
