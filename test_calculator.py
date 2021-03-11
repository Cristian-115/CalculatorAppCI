

import calculator


class TestCalculator:

    def test_add(self):
        assert 6 == calculator.add(5, 1)

    def test_subtract(self):
        assert 6 == calculator.subtract(8, 2)

    def test_multiply(self):
        assert 9 == calculator.subtract(3, 3)
        