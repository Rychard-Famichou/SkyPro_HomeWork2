class Category:
    category_count = 0
    product_count = 0


    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)


    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1


    @property
    def products(self):
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
        return result


    @property
    def products_list(self):
        return self.__products
