from solutions.CHK import checkout


class TestSum():

    def test_illegal_item(self):
        assert checkout("Z") == -1

    def test_item_a(self):
        assert checkout("A") == 50



