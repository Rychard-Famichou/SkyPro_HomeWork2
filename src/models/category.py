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


    def add_product(self, product: "Product") -> None:
        self.__products.append(product)
        Category.product_count += 1


    @property
    def products(self) -> str:
        products_strings = []
        for product in self.__products:
            products_strings.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(products_strings)


    @property
    def products_list(self) -> list["Product"]:
        return self.__products
