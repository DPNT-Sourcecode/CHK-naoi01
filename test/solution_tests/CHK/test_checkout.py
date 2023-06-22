from solutions.SUM import sum_solution
from solutions.CHK import checkout


class TestSum():

    def test_item_a(self):
        assert sum_solution.compute(1, 2) == 3

