from shoplab.domain.models import Order
from shoplab.application.notifier_factory import notifier_for_special_orders


def send_special_confirmation(order: Order) -> None:
    notifier = notifier_for_special_orders()
    notifier.send(order, f"Special handling for {order.order_id}")
