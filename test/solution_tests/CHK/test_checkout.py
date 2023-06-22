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

    def test_item_a_special_offer_multiple_times(self):
        # assume only apply offers once
        assert checkout("AAAAAA") == 280

    def test_item_a_special_offer_short_of_twice(self):
        assert checkout("AAAA") == 180


"""
Result is: FAILED
Some requests have failed (14/24). Here are some of them:
 - {"method":"checkout","params":[""],"id":"CHK_R1_002"}, expected: 0, got: -1
 - {"method":"checkout","params":["ABCD"],"id":"CHK_R1_011"}, expected: 115, got: -1
 - {"method":"checkout","params":["AA"],"id":"CHK_R1_013"}, expected: 100, got: -1
You have received a penalty of: 10 min
"""