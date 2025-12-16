from python_template.utils import add


def test_add() -> None:
    expected_result = 5
    assert add(2, 3) == expected_result
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_add_negative() -> None:
    expected_result = -2
    assert add(-1, -1) == expected_result
