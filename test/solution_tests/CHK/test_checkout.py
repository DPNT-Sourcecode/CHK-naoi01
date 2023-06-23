from parameterized import parameterized
from solutions.CHK import checkout

class TestSum():

    def test_illegal_item(self):
        assert checkout("=") == -1

    def test_item_a(self):
        assert checkout("A") == 50

    def test_item_b(self):
        assert checkout("B") == 30

    def test_item_c(self):
        assert checkout("C") == 20

    def test_item_d(self):
        assert checkout("D") == 15

    def test_item_a_special_offer(self):
        assert checkout("AAA") == 130

    def test_item_b_special_offer(self):
        assert checkout("BB") == 45

    def test_item_a_special_offer__5a_for_200_multiple_times_before_worse_offer(self):
        assert checkout("AAAAAAAAAA") == 400

    def test_item_a_special_offer_short_of_twice(self):
        assert checkout("AAAA") == 180

    def test_item_a_special_offer__5a_for_200(self):
        assert checkout("AAAAA") == 200

    def test_item_e(self):
        assert checkout("E") == 40

    def test_item_e_without_B(self):
        assert checkout("EE") == 80

    def test_item_e_special_offer_with_B(self):
        assert checkout("EEB") == 80

    def test_e_special_offer_twice_prefers_to_use_b_special_offer_first(self):
        # 2E = 80
        assert checkout("EEBEEB") == 160

    def test_b_special_offer_twice_preders_to_use_b_special_offer_over_e(self):
        # 2B = 45
        # 4E = 240
        assert checkout("BEBEEE") == 160

    def test_item_f(self):
        assert checkout("F") == 10

    def test_special_offer_f(self):
        assert checkout("FFF") == 20

    def test_special_offer_f_multi(self):
        assert checkout("FFFF") == 30

    def test(self):
        assert checkout("HHHHH") == 45
        assert checkout("HHHHHH") == 55
        assert checkout("HHHHHHH") == 65

    def test_hanging_on_deploy(self):
        assert checkout("VVV") == 130

    def test_ZZZSSSTTT(self):
        assert checkout("ZZZSSSTTT") == 45*3

    def test_STX(self):
        assert checkout("STX", ) == 45

    def test_STXSTX(self):
        assert checkout("STXSTX") == 90

    def test_SSS(self):
        assert checkout("SSS", ) == 45





"""
 - {"method":"checkout","params":["STX"],"id":"CHK_R5_139"}, expected: 45, got: 57
 - {"method":"checkout","params":["STXSTX"],"id":"CHK_R5_140"}, expected: 90, got: 114
 - {"method":"checkout","params":["SSS"],"id":"CHK_R5_141"}, expected: 45, got: null
"""




