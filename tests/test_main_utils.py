from unittest.mock import MagicMock, patch

import pytest

from utils.main_utils import main


def test_main_with_argument(capsys: pytest.CaptureFixture[str]) -> None:
    # 1. Создаем имитацию объектов Category и Product
    mock_product = MagicMock()
    mock_product.name = "Samsung"
    mock_product.price = 100.0

    mock_category = MagicMock()
    mock_category.name = "Смартфоны"
    mock_category.products_list = [mock_product]

    with patch("utils.main_utils.load_data") as mock_load:
        with patch("utils.main_utils.create_objects") as mock_create:
            # Настраиваем возвращаемые значения моков
            mock_load.return_value = [{"fake": "data"}]
            mock_create.return_value = [mock_category]

            # 3. Запуск функции с любым строковым путем
            main("fake/path/products.json")

            # 4. Проверка вызовов
            mock_load.assert_called_once_with("fake/path/products.json")
            mock_create.assert_called_once()

            # 5. Проверка вывода в консоль
            captured = capsys.readouterr()  # captured будет иметь тип CaptureResult
            assert "Категория: Смартфоны" in captured.out
            assert "Товар: Samsung, Цена: 100.0" in captured.out
