# https://www.acer.com/us-en/laptops
from product import Product
class Computer(Product):
    def __init__(self, name:str, company_name:str, operating_system:str) -> None:
        self._name = name
        self._company_name = company_name
        self._operating_system = operating_system

    # def __str__(self) -> str:
    #     return f"{super(Computer, self).__str__()} | From Product" # Product(Aspire 3 Intel, Acer) | From Product

    # def __str__(self) -> str:
    #     return f"Computer({self._name}, {self._company_name})" # Computer(Aspire 3 Intel, Acer)

    # def get_computer_info(self) -> str:
    
    #     return f"{self._company_name}, {self._name}" # Acer, Aspire 3 Intel

    def get_os_name(self) -> str:
        return self._operating_system

    
    def get_computer_info(self) -> str:
        return f"""
            Company: {self.get_company_name()}
            Name: {self.get_name()}
            Operating system: {self.get_os_name()}
                """

notebook = Computer("Aspire 3 Intel", "Acer", "Windows 10 Home in S mode 64-bit")

# print(notebook.get_name()) # Aspire 3 Intel
# print(notebook.get_company_name()) # Acer
# print(notebook.get_os_name()) # Windows 10 Home in S mode 64-bit
# print(notebook.get_computer_info()) 