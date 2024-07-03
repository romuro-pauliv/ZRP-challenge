# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                    model/api/completion_request.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# |--------------------------------------------------------------------------------------------------------------------|
from tenacity   import wait_random_exponential, stop_after_attempt, retry
from typing     import Union
from json       import dumps

from openai                                                 import OpenAI
from openai.types.chat.chat_completion                      import ChatCompletion
from openai.types.chat.chat_completion_message              import ChatCompletionMessage
from openai.types.chat.chat_completion_message_tool_call    import ChatCompletionMessageToolCall

from app.config.config_vars             import ConfigModel
from app.model.functions.read_functions import gpt_functions
from app.model.data.user_data           import user_data
from app.products.products_manager      import products_manager
from app.log.genlog                     import genlog
from app.utils.json_manager             import JsonManager
# |--------------------------------------------------------------------------------------------------------------------|

CLIENT: OpenAI = OpenAI()


class Completion(JsonManager):
    """
    Manages chat completions with GPT, handling user messages and API requests.
    """
    def __init__(self) -> None:
        """
        Initializes the Completion class by loading the 'init_chat_system' JSON file and setting up user messages.
        """
        self.users_messages: dict[str, list[dict[str, str]]] = {}
        super().__init__("init_chat_system")
        
        self.role_system: list[dict[str, str]] = []
        for role in self.json.values():
            self.role_system.append(role)
        
    @staticmethod
    @retry(wait=wait_random_exponential(multiplier=1, max=60), stop=stop_after_attempt(ConfigModel.REQUEST_STOP_AFTER))
    def request_w_func(messages) -> ChatCompletion:
        """
        Makes a request to the GPT API with the provided messages and handles retries with exponential backoff.
        Args:
            messages (list[dict[str, str]]): The messages to send to the GPT API.
        Returns:
            ChatCompletion: The response from the GPT API.
        """
        try:
            response: ChatCompletion = CLIENT.chat.completions.create(
                model=ConfigModel.GPT_MODEL,
                messages=messages,
                tools=gpt_functions.tools(),
                tool_choice=None
            )
            genlog.log("API", "ChatCompletion GPT API", True)
            return response
        except Exception as e:
            genlog.log(False, "GPT API Error", False)
            print(e)
            return None
    
    def _get_user_messages(self, user_id: str) -> list[dict[str, str]]:
        """
        Retrieves the list of messages for a given user. If the user is new, initializes their message list.
        Args:
            user_id (str): The ID of the user.
        Returns:
            list[dict[str, str]]: The list of messages for the user.
        """
        try:
            messages: list[dict[str, str]] = self.users_messages[user_id]
            genlog.log(True, f"message from [{user_id}]", True)
        except KeyError:
            self.users_messages[user_id] = self.role_system
            messages: list[dict[str, str]] = self.users_messages[user_id]
            genlog.log(True, f"first message from [{user_id}]", True)
            user_data.create_schema(user_id)
        return messages
        
    def send(self, user_id: str, user_message: str) -> None:
        """
        Sends a user message, processes the GPT response, and handles tool calls if necessary.
        Args:
            user_id (str): The ID of the user.
            user_message (str): The message from the user.
        Returns:
            str: message content
        """
        messages: list[dict[str, str]] = self._get_user_messages(user_id)
        messages.append({"role": "user", "content": user_message})
        
        chat_response: ChatCompletion = Completion.request_w_func(messages)
        messages.append(chat_response.choices[0].message)
        
        for _ in range(ConfigModel.TOOL_CALLS_LOOP):
            if messages[-1].tool_calls:
                messages: ChatCompletionMessage = ToolCallTreatment(user_id, messages).answer_calls()
            else:
                break
        
        return messages[-1].content
        
        

class ToolCallTreatment(object):
    def __init__(self, user_id: str, chat: list[dict[str, str]]) -> None:
        self.chat           : list[ChatCompletionMessage]                       = chat
        self.tool_calls_msg : Union[list[ChatCompletionMessageToolCall], None]  = self.chat[-1].tool_calls
        self.user_id        : str                                               = user_id
        
        self.call_func_products: str = "get_products"
        self.call_func_fullname: str = "get_fullname"
        self.call_func_phone_n : str = "get_phone_number"
        self.call_func_email   : str = "get_email"
        self.call_func_order   : str = "get_order"
        self.call_func_pay_met : str = "get_payment_method"
        self.call_func_installm: str = "get_installment"
        self.call_func_remove_o: str = "remove_order"
    
    def _call_products(self, id_: str, function_name: str, arguments: str) -> dict[str, str]:
        arguments: str = dumps(products_manager.get_products(eval(arguments)['category']))
        genlog.log("API CALLS", f"products call [{arguments}]", True)
        return {"role": "tool", "tool_call_id": id_, "name": function_name, "content": arguments}
    
    def _call_fullname(self, id_: str, function_name: str, arguments: str) -> dict[str, str]:
        arguments: str = eval(arguments)['fullname']
        genlog.log("API CALLS", f"fullname call [{arguments}]", True)
        user_data.update_fullname(self.user_id, arguments)
        return {"role": "tool", "tool_call_id": id_,"name": function_name, "content": arguments}
        
    def _call_phonenumber(self, id_: str, function_name: str, arguments: str) -> dict[str, str]:
        arguments: str = eval(arguments)['phone_number']
        genlog.log("API CALLS", f"phone number call [{arguments}]", True)
        user_data.update_phonenumber(self.user_id, arguments)
        return {"role": "tool", "tool_call_id": id_, "name": function_name, "content": arguments}
    
    def _call_email(self, id_: str, function_name: str, arguments: str) -> dict[str, str]:
        arguments: str = eval(arguments)['email']
        genlog.log("API CALLS", f"email call [{arguments}]", True)
        user_data.update_email(self.user_id, arguments)
        return {"role": "tool", "tool_call_id": id_, "name": function_name, "content": arguments}

    def _call_order(self, id_: str, function_name: str, arguments: str) -> dict[str, str]:
        arguments: str = eval(arguments)['product']
        genlog.log("API CALLS", f"order call [{arguments}]", True)
        user_data.update_order(self.user_id, arguments)
        return {"role": "tool", "tool_call_id": id_, "name": function_name, "content": arguments}

    def _call_payment_method(self, id_: str, function_name: str, arguments: str) -> dict[str, str]:
        arguments: str = eval(arguments)['method']
        genlog.log("API CALLS", f"payment method call [{arguments}]", True)
        user_data.update_payment_method(self.user_id, arguments)
        return {"role": "tool", "tool_call_id": id_, "name": function_name, "content": arguments}
    
    def _call_installment(self, id_: str, function_name: str, arguments: str) -> dict[str, str]:
        arguments: str = eval(arguments)['installment']
        genlog.log("API CALLS", f"installment call [{arguments}]", True)
        user_data.update_installments(self.user_id, arguments)
        return {"role": "tool", "tool_call_id": id_, "name": function_name, "content": arguments}

    def _call_remove_order(self, id_: str, function_name: str, arguments: str) -> dict[str, str]:
        arguments: str = eval(arguments)["remove_product"]
        genlog.log("API CALLS", f"remove order [{arguments}]", True)
        user_data.remove_order(self.user_id, arguments)
        return {"role": "tool", "tool_call_id": id_, "name": function_name, "content": arguments}
            
    def answer_calls(self) -> None:
        for calls in self.tool_calls_msg:
            call_id: str = calls.id
            call_func_name: str = calls.function.name
            call_func_args: str = calls.function.arguments
            
            if call_func_name == self.call_func_products:
                self.chat.append(self._call_products(call_id, call_func_name, call_func_args))
            
            if call_func_name == self.call_func_fullname:
                self.chat.append(self._call_fullname(call_id, call_func_name, call_func_args))
            
            if call_func_name == self.call_func_phone_n:
                self.chat.append(self._call_phonenumber(call_id, call_func_name, call_func_args))
            
            if call_func_name == self.call_func_email:
                self.chat.append(self._call_email(call_id, call_func_name, call_func_args))
            
            if call_func_name == self.call_func_order:
                self.chat.append(self._call_order(call_id, call_func_name, call_func_args))
            
            if call_func_name == self.call_func_pay_met:
                self.chat.append(self._call_payment_method(call_id, call_func_name, call_func_args))
            
            if call_func_name == self.call_func_installm:
                self.chat.append(self._call_installment(call_id, call_func_name, call_func_args))
            
            if call_func_name == self.call_func_remove_o:
                self.chat.append(self._call_remove_order(call_id, call_func_name, call_func_args))

        chat_response: ChatCompletion = Completion.request_w_func(self.chat)
        self.chat.append(chat_response.choices[0].message)
        return self.chat
    
    

completion_chat: Completion = Completion()