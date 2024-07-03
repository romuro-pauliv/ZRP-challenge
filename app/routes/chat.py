# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                 api/routes/chat.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# |--------------------------------------------------------------------------------------------------------------------|
from flask import Blueprint, request

from app.model.api.completion_request import completion_chat
# |--------------------------------------------------------------------------------------------------------------------|

bp_chat: Blueprint = Blueprint("chat", __name__)

@bp_chat.route("/", methods=["GET"])
def completion() -> tuple[str, int]:
    message: str = request.json['message']
    user_id: str = request.json['user_id']
    
    chat_response: str = completion_chat.send(user_id, message)
    if chat_response is not None:
        return {"chat": chat_response}, 200
    
    return "chat error", 500