from pytest import raises

from python_template.utils import add


def test_add() -> None:
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    with raises(TypeError):
        assert add("ks", 3) == "ksksks"  # type: ignore
