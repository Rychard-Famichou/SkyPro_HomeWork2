import json
from pathlib import Path
from typing import Any, cast


def load_data(file_path: str) -> list[dict[str, Any]]:
    """Загружает данные из JSON-файла с помощью pathlib"""
    path = Path(file_path)

    # Читаем содержимое файла
    data = path.read_text(encoding='utf-8')

    # Десериализуем JSON
    loaded_data = json.loads(data)

    # Используем cast, чтобы mypy не ругался на Any
    return cast(list[dict[str, Any]], loaded_data)
