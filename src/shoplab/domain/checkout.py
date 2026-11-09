from shoplab.domain.models import Order


def send_special_confirmation(order: Order) -> None:
    from shoplab.infrastructure.console_notifier import ConsoleNotifier
    notifier = ConsoleNotifier()
    notifier.send(order, f"Special handling for {order.order_id}")
