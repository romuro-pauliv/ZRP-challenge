# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                    api/__init__.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# |--------------------------------------------------------------------------------------------------------------------|
from flask import Flask

from app.log.genlog import genlog
# |--------------------------------------------------------------------------------------------------------------------|

genlog.active_verbose()
genlog.active_color()

def create_app() -> Flask:
    app: Flask = Flask(__name__)
    
    from .routes.chat import bp_chat
    app.register_blueprint(bp_chat, url_prefix="/chat")
    
    from .routes.products import bp_products
    app.register_blueprint(bp_products, url_prefix="/products")
    
    return app