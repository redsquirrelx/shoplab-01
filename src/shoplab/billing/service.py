from dataclasses import dataclass
from shoplab.domain.models import Order
from shoplab.domain.pricing import order_total
from shoplab.inventory import _store


@dataclass(frozen=True)
class Receipt:
    order_id: str
    amount: int
    stock_checked: int


def _stock_for_charge(sku: str) -> int:
    return _store.STOCK.get(sku, 0)


def charge(order: Order) -> Receipt:
    # A payment module is reading another module's concrete backing state.
    units = _stock_for_charge(order.sku)
    return Receipt(order.order_id, order_total(order), units)
