from shoplab.domain.models import Order


def special_confirmation_message(order: Order) -> str:
    return f"Special handling for {order.order_id}"
