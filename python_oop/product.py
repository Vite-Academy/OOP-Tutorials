class Product:
    """Creating a new product for me"""

    # Class attribute
    goal = "Production of new products"
    
    def __init__(self, name, company_name:str) -> None:
        # Class attribute
        self._placeholder = "Product"

        self._name = name
        self._company_name = company_name


# print(Product._placeholder) # AttributeError
print(Product.goal) # Production of new products