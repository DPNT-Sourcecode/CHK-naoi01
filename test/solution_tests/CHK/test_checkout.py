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
        assert checkout("A, A, A") == 130

    def test_item_b_special_offer(self):
        assert checkout("B, B") == 45
