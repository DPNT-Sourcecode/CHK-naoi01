from typing import NamedTuple, Callable


class IllegalItem(Exception):
    pass


class SKU(NamedTuple):
    name: str
    price: int


class SpecialOffer(NamedTuple):
    name: str
    should_apply: Callable[[list[SKU]], bool]
    skus_to_remove: list[SKU]
    reduced_price: int
    discount: int


A = SKU("A", 50)
B = SKU("B", 30)
C = SKU("C", 20)
D = SKU("D", 15)
E = SKU("E", 40)
F = SKU("F", 10)
G = SKU("G", 20)
H = SKU("H", 10)
I = SKU("I", 35)
J = SKU("J", 60)
K = SKU("K", 70)
L = SKU("L", 90)
M = SKU("M", 15)
N = SKU("N", 40)
O = SKU("O", 10)
P = SKU("P", 50)
Q = SKU("Q", 30)
R = SKU("R", 50)
S = SKU("S", 20)
T = SKU("T", 20)
U = SKU("U", 40)
V = SKU("V", 50)
W = SKU("W", 20)
X = SKU("X", 17)
Y = SKU("Y", 20)
Z = SKU("Z", 21)

SKU_STR_TO_ITEMS = {
    "A": A,
    "B": B,
    "C": C,
    "D": D,
    "E": E,
    "F": F,
    "G": G,
    "H": H,
    "I": I,
    "J": J,
    "K": K,
    "L": L,
    "M": M,
    "N": N,
    "O": O,
    "P": P,
    "Q": Q,
    "R": R,
    "S": S,
    "T": T,
    "U": U,
    "V": V,
    "W": W,
    "X": X,
    "Y": Y,
    "Z": Z,
}

SPECIAL_OFFERS = [
    SpecialOffer(
        name="5A for 200",
        should_apply=lambda skus: skus.count(A) >= 5,
        skus_to_remove=[A, A, A, A, A],
        reduced_price=200,
        discount=50,
    ),
    SpecialOffer(
        name="3A for 130",
        should_apply=lambda skus: skus.count(A) >= 3,
        skus_to_remove=[A, A, A],
        reduced_price=130,
        discount=20,
    ),
    SpecialOffer(
        name="2B for 45",
        should_apply=lambda skus: skus.count(B) >= 2,
        skus_to_remove=[B, B],
        reduced_price=45,
        discount=15,
    ),
    SpecialOffer(
        name="2E get one B free",
        should_apply=lambda skus: skus.count(E) >= 2 and skus.count(B) >= 1,
        skus_to_remove=[E, E, B],
        reduced_price=80,
        discount=B.price,
    ),
    SpecialOffer(
        name="2F get one F free",
        should_apply=lambda skus: skus.count(F) >= 3,
        skus_to_remove=[F, F, F],
        reduced_price=20,
        discount=10,
    ),
    SpecialOffer(
        name="10H for 80",
        should_apply=lambda skus: skus.count(H) >= 10,
        skus_to_remove=[H] * 10,
        reduced_price=80,
        discount=20,
    ),
    SpecialOffer(
        name="5H for 45",
        should_apply=lambda skus: skus.count(H) >= 5,
        skus_to_remove=[H] * 5,
        reduced_price=45,
        discount=5,
    ),
    SpecialOffer(
        name="2K for 120",
        should_apply=lambda skus: skus.count(K) >= 2,
        skus_to_remove=[K] * 2,
        reduced_price=120,
        discount=40,
    ),
    SpecialOffer(
        name="3N get one M free",
        should_apply=lambda skus: skus.count(N) >= 3 and skus.count(M) >= 1,
        skus_to_remove=[N, N, N, M],
        reduced_price=120,
        discount=15,
    ),
    SpecialOffer(
        name="5P for 200",
        should_apply=lambda skus: skus.count(P) >= 5,
        skus_to_remove=[P] * 5,
        reduced_price=200,
        discount=50,
    ),
    SpecialOffer(
        name="3Q for 80",
        should_apply=lambda skus: skus.count(Q) >= 3,
        skus_to_remove=[Q] * 3,
        reduced_price=80,
        discount=10,
    ),
    SpecialOffer(
        name="3R get one Q free",
        should_apply=lambda skus: skus.count(R) >= 3 and skus.count(Q) >= 1,
        skus_to_remove=[R, R, R, Q],
        reduced_price=150,
        discount=30,
    ),
    SpecialOffer(
        name="3U get one U free",
        should_apply=lambda skus: skus.count(U) >= 4,
        skus_to_remove=[U] * 4,
        reduced_price=120,
        discount=40,
    ),
    SpecialOffer(
        name="2V for 90",
        should_apply=lambda skus: skus.count(V) >= 2,
        skus_to_remove=[V, V],
        reduced_price=90,
        discount=10,
    ),
    SpecialOffer(
        name="3V for 130",
        should_apply=lambda skus: skus.count(V) >= 3,
        skus_to_remove=[V] * 3,
        reduced_price=130,
        discount=20,
    ),

    # Group discounts
    # +------+-------+---------------------------------+
    # | Item | Price | Special offers                  |
    # +------+-------+---------------------------------+
    # | S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    # | T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    # | X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
    # | Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    # | Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
    # +------+-------+---------------------------------+
    SpecialOffer(
        name="buy any 3 of (S,T,X,Y,Z) for 45",
        should_apply=lambda skus: skus.count(V) >= 3,
        skus_to_remove=[V] * 3,
        reduced_price=130,
        discount=20,
    ),

]


def parse_skus(skus: str) -> list[SKU]:
    """Takes a unicode str representing the basket and returns a list of SKUs

    Examples:
        >>> parse_skus("AAAA")
        ... [A, A, A, A]

    Raises:
        IllegalItem if item is not known to the shop
    """
    sku_objects = []
    for sku_str in list(skus):
        if sku_str not in SKU_STR_TO_ITEMS:
            raise IllegalItem
        sku_objects.append(SKU_STR_TO_ITEMS[sku_str])
    return sku_objects


def remove_skus_in_offer_from_remaining_basket(offer: SpecialOffer, current_basket: list[SKU]) -> list[SKU]:
    remove_skus = offer.skus_to_remove
    for item in remove_skus:
        # value error shouldn't be raised as we have already checked offer applies
        index_of_item = current_basket.index(item)
        current_basket.pop(index_of_item)
    return current_basket


def basket_contains_applicable_offers(current_basket: list[SKU]) -> bool:
    for offer in SPECIAL_OFFERS:
        if offer.should_apply(current_basket):
            return True

    return False


def choose_best_offer_to_apply(current_basket: list[SKU]) -> SpecialOffer:
    """i.e. choose offer that gives customer the largest discount"""
    applicable_offers = [offer for offer in SPECIAL_OFFERS if offer.should_apply(current_basket)]
    offer_with_largest_discount = sorted(applicable_offers, key=lambda offer: offer.discount, reverse=True)[0]
    return offer_with_largest_discount


# skus = unicode string
def checkout(skus: str) -> int:
    try:
        basket_items = parse_skus(skus)
    except IllegalItem:
        return -1

    total_checkout_value = 0

    # First apply offers (which could be applicable multiple times)
    while basket_contains_applicable_offers(basket_items):
        best_offer = choose_best_offer_to_apply(basket_items)
        total_checkout_value += best_offer.reduced_price
        basket_items = remove_skus_in_offer_from_remaining_basket(best_offer, basket_items)

    # Go through remaining items after offers have been applied
    for item in basket_items:
        total_checkout_value += item.price
    return total_checkout_value





