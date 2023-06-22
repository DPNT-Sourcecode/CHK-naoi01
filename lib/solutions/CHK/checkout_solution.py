from typing import NamedTuple


class IllegalItem(Exception):
    pass


class BasketItem(NamedTuple):
    name: str
    price: int


SKU_TO_ITEMS = {
    "A": BasketItem("A", 50),
    "B": BasketItem("B", 30),
    "C": BasketItem("C", 20),
    "D": BasketItem("D", 15),
}


def parse_skus(skus: str) -> list[BasketItem]:
    """Takes a comma seperated str representing the basket and returns a list of BasketItems

    Raises:
        IllegalItem if item is not known to the shop
    """
    sku_objects = []
    for sku_str in skus.split(","):
        if sku_str not in SKU_TO_ITEMS:
            raise IllegalItem
        sku_objects.append(SKU_TO_ITEMS[sku_str])
    return sku_objects


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    try:
        basket_items = parse_skus(skus)
    except IllegalItem:
        return -1

    return 0




