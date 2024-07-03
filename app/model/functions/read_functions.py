# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                  model/functions/read_functions.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# |--------------------------------------------------------------------------------------------------------------------|
from app.utils.json_manager         import JsonManager
from app.products.products_manager  import products_manager

from app.log.genlog import genlog

from typing import Any
# |--------------------------------------------------------------------------------------------------------------------|

class GPTFunctions(JsonManager):
    def __init__(self) -> None:
        """
        Initializes the GPTFunctions by loading the 'gpt_functions' JSON file and updating the function 
        configurations.
        """
        super().__init__("gpt_functions")
        self.update_functions()
        
    def _concat(self) -> None:
        """
        Concatenates the JSON values into a list of function configurations and logs each function creation.
        """
        self.func: list[dict[str, Any]] = []
        for i in self.json.values():
            self.func.append(i)
            genlog.log(True, f"create GPT function: {i['function']['name']}", True)
    
    def _append_categories(self) -> None:
        """
        Appends the product categories to the first function's category enumeration in the function 
        configurations and logs the operation.
        """
        categories: list[str] = products_manager.get_categories()['categories']
        self.func[0]["function"]["parameters"]["properties"]["category"]["enum"] = categories
        genlog.log(True, "append categories in GPT function", True)
        
    def update_functions(self) -> None:
        """
        Updates the function configurations by calling internal methods to concatenate JSON values 
        and append categories.
        """
        self._concat()
        self._append_categories()
    
    def tools(self) -> list[dict[str, Any]]:
        """
        Retrieves the current list of function configurations.

        Returns:
            list[dict[str, Any]]: A list of function configurations.
        """
        return self.func


gpt_functions: GPTFunctions = GPTFunctions()