# https://pynative.com/
class Product:
    """Creating a new product for me"""

    # Class attribute
    goal = "Production of new products"

    def __init__(self, name:str, company_name:str) -> None:
        # Class attribute
        self._placeholder = "Product"

        self._name = name
        self._company_name = company_name

    # @staticmethod
    # def get_name(self):
    #     return self._name # TypeError


    # def get_name(self):
    #     return self._name # Product name


# print(Product._placeholder) # AttributeError
# print(Product.goal) # Production of new products

product = Product("Product name", "Company name")
print(product.get_name())