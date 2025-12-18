from {{ project_name | snake_case }}.utils import add


def test_add() -> None:
    """Test the add function."""
    expected_result = 5
    assert add(2, 3) == expected_result
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_add_negative() -> None:
    """Test the add function with negative numbers."""
    expected_result = -2
    assert add(-1, -1) == expected_result
