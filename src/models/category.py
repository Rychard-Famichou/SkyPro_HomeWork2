from models.product import Product


class Category:
    """ Custom class:
    Название
    Описание
    Список объектов класса Product
    """
    category_count = 0
    product_count = 0


    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """ Создание объекта класса, для добавления Product используем метод-проверку add_product """
        self.name = name
        self.description = description
        self.__products: list[Product] = []
        Category.category_count += 1

        for p in products:
            self.add_product(p)


    def __str__(self) -> str:
        """ Возвращает строку класса """
        all_products_count = 0
        for product in self.__products:
            all_products_count += product.quantity
        return f"{self.name}, количество продуктов: {all_products_count} шт."


    def add_product(self, product: Product) -> None:
        """ Добавляет новый продукт в список и обновляет счетчик """
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Добавлять можно только объекты классов Product или его наследников")


    @property
    def products(self) -> str:
        """ Возвращает строку каждого продукта """
        return "\n".join(map(str, self.__products))


    @property
    def products_list(self) -> list[Product]:
        """ Возвращает список продуктов """
        return self.__products
