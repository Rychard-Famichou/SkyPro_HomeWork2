import pytest
from _pytest.capture import CaptureFixture

from models.order import Order
from models.product import Product
from models.product_smartphone import Smartphone
from models.zero_except import ZeroQuantityError


def test_order_creation_success(sample_products: tuple[Smartphone, Smartphone], capsys: CaptureFixture[str]) -> None:
    """Тест успешного создания заказа и списания остатков"""
    iphone, _ = sample_products

    order = Order("iPhone 15", 3)
    print(order)
    captured = capsys.readouterr()
    expected_output = "Заказ на iPhone 15 в количестве 3 шт."

    assert expected_output in captured.out
    assert order.total_price == 3000.0
    assert iphone.quantity == 7


def test_order_insufficient_stock(sample_products: tuple[Smartphone, Smartphone]) -> None:
    """Тест заказа количества больше, чем есть на складе"""
    _, samsung = sample_products

    order = Order("Samsung S23", 10)

    assert order.total_price == 0.0
    assert samsung.quantity == 5  # Остаток не должен измениться


def test_order_product_not_found(sample_products: tuple[Smartphone, Smartphone]) -> None:
    """Тест заказа несуществующего товара"""
    order = Order("Nokia 3310", 1)

    assert order.total_price == 0.0


def test_mixin_registration() -> None:
    """Тест, что Mixin действительно добавляет товар в Order.all_products"""
    Product("Samsung S23", "Android", 800.0, 5)

    assert len(Order.all_products) == 1
    assert Order.all_products[0].name == "Samsung S23"


def test_order_products(sample_products: tuple[Smartphone, Smartphone], capsys: CaptureFixture[str]) -> None:
    """Тест вывода products"""
    order = Order("iPhone 15", 5)
    print(order.products)
    captured = capsys.readouterr()
    expected_output = "iPhone 15, 1000.0 руб. Остаток: 5 шт.\nSamsung S23, 800.0 руб. Остаток: 5 шт."

    assert expected_output in captured.out


def test_zero_quantity() -> None:
    """Тест 0 количество"""
    with pytest.raises(ZeroQuantityError) as excinfo:
        _ = Order("iPhone 15", 0)

    assert str(excinfo.value) == "Товар с нулевым количеством не может быть добавлен"
