from pathlib import Path

from utils.loaders import load_data


def test_load_data_pathlib(tmp_path: Path) -> None:
    # Создаем файл во временной директории
    file = tmp_path / "test_products.json"
    content = '[{"name": "Apple", "price": 100}]'
    file.write_text(content, encoding="utf-8")

    # Вызываем функцию
    result = load_data(str(file))

    assert len(result) == 1
    assert result[0]["name"] == "Apple"
