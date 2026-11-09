from shoplab.inventory import _store


def raw_available_units(sku: str) -> int:
    return _store.STOCK.get(sku, 0)
