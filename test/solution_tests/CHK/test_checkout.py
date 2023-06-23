from solutions.CHK import checkout


class TestSum():

    def test_illegal_item(self):
        assert checkout("Z") == -1

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


