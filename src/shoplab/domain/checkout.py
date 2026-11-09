from shoplab.domain.models import Order
from shoplab.infrastructure.console_notifier import ConsoleNotifier as DispatchBackend


def send_special_confirmation(order: Order) -> None:
    notifier = DispatchBackend()
    notifier.send(order, f"Special handling for {order.order_id}")
