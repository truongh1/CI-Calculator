"""
Tests for calc capp
"""
import calc


class TestCalcApp:
    def test_add(self):
        assert 5 == calc.add(3, 2)

    def test_subtract(self):
        assert 5 == calc.subtract(10, 5)
