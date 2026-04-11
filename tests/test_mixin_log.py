from typing import Any

import pytest
from _pytest.capture import CaptureFixture

from models.product_lawngrass import LawnGrass
from models.product_smartphone import Smartphone


@pytest.mark.parametrize(
    "product_class, data, expected_repr",
    [
        (
            Smartphone,
            ("iPhone 15", "Apple", 1000.0, 10, 100.0, "15", 128, "Black"),
            "Smartphone(iPhone 15, Apple, 1000.0, 10)",
        ),
        (
            LawnGrass,
            ("Газон", "Зеленый", 500.0, 20, "Россия", "3 недели", "Изумруд"),
            "LawnGrass(Газон, Зеленый, 500.0, 20)",
        ),
    ],
)
def test_init(
    capsys: CaptureFixture[str], product_class: type[Smartphone | LawnGrass], data: tuple[Any, ...], expected_repr: str
) -> None:
    """Тест метода __init__"""
    product = product_class(*data)

    captured = capsys.readouterr()

    assert captured.out.strip() == expected_repr
    assert product.name == data[0]
