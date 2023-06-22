from typing import NamedTuple, Callable


class IllegalItem(Exception):
    pass


class SKU(NamedTuple):
    name: str
    price: int


class SpecialOffer(NamedTuple):
    name: str
    applicable_sku: SKU
    should_apply_offer: Callable
    apply_offer: Callable


A = SKU("A", 50)
B = SKU("B", 30)
C = SKU("C", 20)
D = SKU("D", 15)

SKU_TO_ITEMS = {
    "A": A,
    "B": B,
    "C": C,
    "D": D,
}

SPECIAL_OFFERS = [
    SpecialOffer(
        name="3A for 130",
        applicable_sku=A,
        should_apply_offer=lambda skus: skus.count(A) == 3,
        apply_offer=lambda skus: 1
    ),
    SpecialOffer(
        name="2B for 45",
        applicable_sku=B,
        should_apply_offer=lambda skus: skus.count(B) == 2,
        apply_offer=lambda skus: 1
    )
]


def parse_skus(skus: str) -> list[SKU]:
    """Takes a comma seperated str representing the basket and returns a list of SKUs

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

    total_checkout_value = 0

    should_apply_offers = [offer.should_apply_offer(basket_items) for offer in SPECIAL_OFFERS]

    for item in basket_items:
        total_checkout_value += item.price

    return total_checkout_value

