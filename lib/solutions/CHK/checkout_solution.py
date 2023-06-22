from typing import NamedTuple, Callable


class IllegalItem(Exception):
    pass


class BasketItem(NamedTuple):
    name: str
    price: int


class SpecialOffer(NamedTuple):
    name: str
    applicable_sku: str
    apply_offer: Callable


SKU_TO_ITEMS = {
    "A": BasketItem("A", 50),
    "B": BasketItem("B", 30),
    "C": BasketItem("C", 20),
    "D": BasketItem("D", 15),
}

SPECIAL_OFFERS = [
    SpecialOffer(
        name="3A for 130",
        applicable_sku="A",
        apply_offer=lambda skus: skus.count
    )
]


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


def special_offer_applicable():
    pass


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    try:
        basket_items = parse_skus(skus)
    except IllegalItem:
        return -1

    total_checkout_value = 0

    for item in basket_items:
        total_checkout_value += item.price

    return total_checkout_value
