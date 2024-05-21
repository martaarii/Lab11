from dataclasses import dataclass
from datetime import  datetime
@dataclass
class Prodotto():
    product_number : int
    product_line : str
    product : str
    product_brand : str
    product_color : str
    unit_cost : float
    unit_price : float

    def  __str__(self):
        return f"{self.product_number} - {self.product}"
    def __hash__(self):
        return f"{self.product_number}"

@dataclass
class Vendita():
    Date : datetime
    Retailer_code : int
    Product_number : int
    def __hash__(self):
        return f"{self.Product_number}"

