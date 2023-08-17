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
    
    def __str__(self) -> str:
        return f"Product({self._name}, {self._company_name})"


    # @staticmethod
    # def get_name(self) -> str:
    #     return self._name # TypeError


    def get_name(self) -> str:
        return self._name # Product name

    def get_company_name(self) -> str:
        return self._company_name # Company name


# print(Product._placeholder) # AttributeError
# print(Product.goal) # Production of new products


product = Product("Product name", "Company name")
# print(product.get_name())
# print(product.get_company_name())


# Without __str__ method
# print(product) # <__main__.Product object at 0x7f84789a6490>
# With __str__ method
# print(product) # Product(Product name, Company name)