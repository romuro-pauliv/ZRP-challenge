# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                            model/data/user_data.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# |--------------------------------------------------------------------------------------------------------------------|
from app.utils.json_manager import JsonManager
# |--------------------------------------------------------------------------------------------------------------------|


class UserData(JsonManager):
    def __init__(self) -> None:
        super().__init__("orders")

        self.schema: dict[str, str] = {
            "fullname": "",
            "phone_number": "",
            "email": "",
            "order": [],
            "payment method": "",
            "installments": ""
        }
        
    def create_schema(self, user_id: str) -> None:
        self.json[user_id] = self.schema
        self.update(self.json)
    
    def update_fullname(self, user_id: str, data: str) -> None:
        self.json[user_id]["fullname"] = data
        self.update(self.json)
    
    def update_phonenumber(self, user_id: str, data: str) -> None:
        self.json[user_id]['phone_number'] = data
        self.update(self.json)
    
    def update_email(self, user_id: str, data: str) -> None:
        self.json[user_id]['email'] = data
        self.update(self.json)
    
    def update_order(self, user_id: str, data: str) -> None:
        self.json[user_id]["order"].append(data)
        self.update(self.json)
        
    def update_payment_method(self, user_id: str, data: str) -> None:
        self.json[user_id]["payment method"] = data
        self.update(self.json)
    
    def update_installments(self, user_id: str, data: str) -> None:
        self.json[user_id]["installments"] = data
        self.update(self.json)
    
    def remove_order(self, user_id: str, data: str) -> None:
        try:
            self.json[user_id]['order'].remove(data)
            self.update(self.json)
        except Exception as e:
            pass
        


user_data: UserData = UserData()