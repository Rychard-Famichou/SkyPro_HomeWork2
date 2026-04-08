from config import PRODUCTS_JSON_FILE
from utils.converters import create_objects
from utils.loaders import load_data


def main(file_path: str) -> None:
    """Отдельный main для доп. задания"""
    # 1. Загружаем данные из файла
    raw_data = load_data(file_path)

    # 2. Создаем объекты
    categories = create_objects(raw_data)

    # 3. Работаем с объектами
    for category in categories:
        print(f"Категория: {category.name}")
        for product in category.products_list:
            print(f" - Товар: {product.name}, Цена: {product.price}")


if __name__ == "__main__":
    main(str(PRODUCTS_JSON_FILE))
