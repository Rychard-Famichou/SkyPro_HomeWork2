from typing import Any, Union

import pytest
from _pytest.capture import CaptureFixture
from _pytest.monkeypatch import MonkeyPatch
from pytest_lazy_fixtures import lf

from models.product import Product
from models.product_lawngrass import LawnGrass
from models.product_smartphone import Smartphone


def test_init(product_iphone: Product) -> None:
    """Тест метода __init__"""
    assert product_iphone.name == "iPhone 15"
    assert product_iphone.description == "Apple"
    assert product_iphone.price == 1000.0
    assert product_iphone.quantity == 10


def test_init_zero_quantity() -> None:
    """Тест метода __init__ с нулевым количеством"""
    with pytest.raises(ValueError) as excinfo:
        _ = Product("iPhone 6", "Old", 100.0, 0)

    assert str(excinfo.value) == "Товар с нулевым количеством не может быть добавлен"


@pytest.mark.parametrize(
    "product_1, product_2, expected",
    [
        (lf("product_iphone"), lf("product_samsung"), 14000.0),
        (lf("product_xiaomi"), lf("product_nokia"), 14000.0),
    ],
)
def test_add_success(
    product_1: Union[Product, Smartphone], product_2: Union[Product, Smartphone], expected: float
) -> None:
    """Тест метода __add__: успех"""
    assert product_1 + product_2 == expected


def test_add_error(product_iphone: Smartphone, product_rus_grass: LawnGrass) -> None:
    """Тест метода __add__: ошибка"""
    with pytest.raises(TypeError) as excinfo:
        _ = product_iphone + product_rus_grass

    assert str(excinfo.value) == "Можно складывать только продукты одного класса"


class TestProductNewProduct:
    """Группа тестов для метода создания и обновления продукта"""

    def test_creation_success(self, product_nokia_dict: dict[str, Any]) -> None:
        """Проверка обычного создания объекта без списка"""
        new_obj = Product.new_product(product_nokia_dict)

        assert isinstance(new_obj, Product)
        assert new_obj.name == "Nokia 3310"

    def test_update_existing_in_list(self, product_iphone: Product) -> None:
        """Проверка обновления, если товар уже есть в списке"""
        products_list = [product_iphone]
        data = {"name": "iPhone 15", "description": "Apple", "price": 1200.0, "quantity": 5}

        result = Product.new_product(data, products_list)

        assert result is product_iphone
        assert result.quantity == 15
        assert result.price == 1200.0

    def test_empty_list_message(self, product_nokia_dict: dict[str, Any], capsys: CaptureFixture[str]) -> None:
        """Проверка вывода сообщения при пустом списке []"""
        Product.new_product(product_nokia_dict, [])
        captured = capsys.readouterr()

        assert "Объект класса создан, но список пуст" in captured.out

    def test_not_in_list_creates_new(self, product_iphone: Product, product_nokia_dict: dict[str, Any]) -> None:
        """Проверка: если в списке нет совпадений, создается новый объект"""
        products_list = [product_iphone]

        result = Product.new_product(product_nokia_dict, products_list)

        assert result is not product_iphone
        assert result.name == "Nokia 3310"


class TestProductPrice:
    """Группа тестов для метода работы с ценой"""

    def test_price_setter(self, product_iphone: Product) -> None:
        """Тест сеттера цены: стандартное поведение"""
        product_iphone.price = 1100.0

        assert product_iphone.price == 1100.0

    @pytest.mark.parametrize("wrong_price", [-100.0, 0.0])
    def test_price_setter_invalid(
        self, product_iphone: Product, capsys: CaptureFixture[str], wrong_price: float
    ) -> None:
        """Тест сеттера цены: отрицательное значение и ноль"""
        product_iphone.price = wrong_price
        captured = capsys.readouterr()

        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product_iphone.price == 1000.0

    @pytest.mark.parametrize(
        "user_input, expected_price, expected_output",
        [
            ("y", 800.0, "Новая цена ниже старой."),  # Подтвердил снижение
            ("n", 1000.0, "Новая цена ниже старой."),  # Отклонил снижение
        ],
    )
    def test_price_setter_confirmation(
        self,
        product_iphone: Product,
        monkeypatch: MonkeyPatch,
        capsys: CaptureFixture[str],
        user_input: str,
        expected_price: float,
        expected_output: str,
    ) -> None:
        """Тест сеттера цены: проверка ввода и сообщений в консоли при понижении цены"""

        # Имитируем ввод пользователя
        monkeypatch.setattr("builtins.input", lambda _: user_input)

        # Пытаемся снизить цену
        product_iphone.price = 800.0

        # Читаем вывод в консоли
        captured = capsys.readouterr()

        # Проверки
        assert expected_output in captured.out
        assert product_iphone.price == expected_price
