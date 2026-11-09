from shoplab.domain.models import Order
from shoplab.domain.ports import Notifier


def send_special_confirmation(order: Order, notifier: Notifier) -> None:
    notifier.send(order, f"Special handling for {order.order_id}")
