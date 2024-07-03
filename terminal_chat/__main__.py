from colorama   import Fore
from uuid       import uuid4
import requests


user_id: str = str(uuid4())


def chat(message: str) -> str:
    response: requests.Response = requests.get(
        "http://127.0.0.1:5000/chat/", json={"user_id": user_id, "message": message}
    )
    
    return response.json()['chat']

print(f"{Fore.YELLOW}>>> {chat('Se aprensente e me conte o que você faz')}")

while True:
    msg: str = input(f"{Fore.CYAN}>>> ")
    response: str = chat(msg)
    print(f"{Fore.YELLOW}>>> {response} \n")