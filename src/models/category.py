from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.product import Product

class Category:
    category_count = 0
    product_count = 0


    def __init__(self, name: str, description: str, products: list["Product"]) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)


    def __str__(self) -> str:
        all_products_count = 0
        for product in self.__products:
            all_products_count += product.quantity
        return f"{self.name}, количество продуктов: {all_products_count} шт."


    def add_product(self, product: "Product") -> None:
        self.__products.append(product)
        Category.product_count += 1


    @property
    def products(self) -> str:
        return "\n".join(map(str, self.__products))


    @property
    def products_list(self) -> list["Product"]:
        return self.__products
