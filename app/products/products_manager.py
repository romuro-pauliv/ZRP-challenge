# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                   api/products/products_manager.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from app.utils.json_manager import JsonManager

from app.log.genlog import genlog

from typing import Union
import copy
# |--------------------------------------------------------------------------------------------------------------------|

PRODUCT_TYPE = dict[str, dict[str, Union[str, float]]]

class ProductsManager(JsonManager):
    """
    Manages product categories and products within those categories using a JSON file as storage.
    """
    def __init__(self) -> None:
        """
        Initializes the ProductsManager by loading the 'products' JSON file.
        """
        super().__init__("products")
    
    def get_categories(self) -> dict[str, list[str]]:
        """
        Retrieves the list of product categories.
        Returns:
            dict[str, list[str]]: A dictionary with a single key "categories" containing a list of category names.
        """
        return {"categories": list(self.json.keys())}
    
    def get_products(self, category: str) -> Union[PRODUCT_TYPE, dict]:
        """
        Retrieves the products in the specified category.
        Args:
            category (str): The name of the category to retrieve products from.
        Returns:
            Union[PRODUCT_TYPE, dict]: A dictionary of products within the specified category, or an 
                                       empty dictionary if the category does not exist.
        """
        try:
            return self.json[category]
        except KeyError:
            return {}
    
    def post_category(self, category_name: str) -> None:
        """
        Adds a new category to the JSON file.
        Args:
            category_name (str): The name of the category to add.
        """
        if category_name not in self.get_categories()["categories"]:
            self.write_backup()
            new_j = copy.deepcopy(self.json)
            new_j[category_name] = {}
            self.update(new_j)
            genlog.log(True, f"create category [{category_name}]", True)
            return None
        genlog.log(False, f"category [{category_name}] already exists", True)
    
    def post_product(self, category: str, product: PRODUCT_TYPE) -> None:
        """
        Adds a new product to the specified category.
        Args:
            category (str): The name of the category to add the product to.
            product (PRODUCT_TYPE): A dictionary representing the product to add.
        """
        try:
            products_names: list[str] = list(self.json[category].keys())
        except KeyError:
            self.post_category(category)
            products_names: list[str] = list(self.json[category].keys())
        
        new_product_name: str = list(product.keys())[0]
        
        if new_product_name not in products_names:
            self.write_backup()
            new_j = copy.deepcopy(self.json)
            new_j[category].update(product)
            self.update(new_j)
            genlog.log(True, f"create product [{new_product_name}]", True)
            return None

        genlog.log(False, f"product name [{new_product_name}] already exists", True)
        
        
        
products_manager: ProductsManager = ProductsManager()