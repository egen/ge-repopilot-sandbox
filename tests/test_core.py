import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from calc import total, maximum


def test_total_positive():
    assert total([1, 2, 3]) == 6


def test_total_with_negative():
    # Fails until the planted bug is fixed.
    assert total([5, -2, 3]) == 6


def test_maximum():
    assert maximum([4, 9, 1]) == 9
    assert maximum([]) is None
