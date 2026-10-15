import pytest

from calculator import add, div, mult, npv, pv, simple_interest, sub


def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(0, 0) == 0


def test_sub():
    assert sub(10, 4) == 6
    assert sub(4, 10) == -6
    assert sub(5, 5) == 0


def test_mult():
    assert mult(3, 4) == 12
    assert mult(-2, 3) == -6
    assert mult(5, 0) == 0


def test_div():
    assert div(9, 3) == 3
    assert div(1, 4) == 0.25
    assert div(-8, 2) == -4


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(5, 0)


def test_financial():
    assert pv(0.05, 10, 0, fv=10000) == pytest.approx(6139.13, abs=0.01)
    assert npv(0.10, [-1000, 300, 400, 500]) == pytest.approx(-19.12, abs=0.01)
    assert simple_interest(1000, 0.05, 3) == pytest.approx(150)
