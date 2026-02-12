from app import calculate_total
def test_calc():
    assert calculate_total(100, 0.05) == 105
