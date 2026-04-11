from models.base_category import BaseCategory
from models.product import Product
from models.zero_except import ZeroExcept


class Category(BaseCategory):
    """Custom class:
    Название
    Описание
    Список объектов класса Product
    """

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """Создание объекта класса, для добавления Product используем метод-проверку add_product"""
        self.name = name
        self.description = description
        self.__products: list[Product] = []
        Category.category_count += 1

        for p in products:
            self.add_product(p)

    def __str__(self) -> str:
        """Возвращает строку класса"""
        all_products_count = 0
        for product in self.__products:
            all_products_count += product.quantity
        return f"{self.name}, количество продуктов: {all_products_count} шт."

    def middle_price(self) -> float:
        """
        Возвращает среднюю цену.
        Если товар один — учитывает его количество.
        Если товаров много — среднее арифметическое их цен.
        """

        try:
            if not self.products_list:
                return round(1 / len(self.products_list), 2)

            elif len(self.products_list) == 1:
                product = self.products_list[0]
                return round((product.price * product.quantity) / product.quantity, 2)

            else:
                total_prices = sum(p.price for p in self.products_list)
                return round(total_prices / len(self.products_list), 2)

        except ZeroDivisionError:
            return 0.0

    def add_product(self, product: Product) -> None:
        """Добавляет новый продукт в список с обработкой исключений, обновляет счётчик"""
        try:
            if not isinstance(product, Product):
                raise TypeError("Добавлять можно только объекты классов Product или его наследников")

            if product.quantity == 0:
                raise ZeroExcept()

        except TypeError as e:
            print(e)
            raise e

        except ZeroExcept as e:
            print(e)
            raise e

        else:
            self.__products.append(product)
            Category.product_count += 1
            print("Продукт добавлен")

        finally:
            print("Процедура добавления продукта завершена")

    @property
    def products(self) -> str:
        """Возвращает строку каждого продукта в категории"""
        return "\n".join(map(str, self.__products))

    @property
    def products_list(self) -> list[Product]:
        """Возвращает список продуктов"""
        return self.__products
