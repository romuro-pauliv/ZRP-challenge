# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                             api/routes/products.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# |--------------------------------------------------------------------------------------------------------------------|
from flask import Blueprint, request

from app.products.products_manager import products_manager

from app.model.functions.read_functions import gpt_functions
# |--------------------------------------------------------------------------------------------------------------------|

bp_products: Blueprint = Blueprint("products", __name__)

@bp_products.route("/add_category", methods=["POST"])
def add_category() -> tuple[str, int]:
    new_category: str = request.json['category']
    products_manager.post_category(new_category)
    return "OK", 202

@bp_products.route("/add_product", methods=["POST"])
def add_product() -> tuple[str, int]:
    category: str = request.json['category']
    product: dict[str, str] = request.json['product']
    products_manager.post_product(category, product)
    gpt_functions.update_functions()
    return "OK", 202

@bp_products.route("/all_categories", methods=["GET"])
def all_categories() -> tuple[dict[str, list[str]], int]:
    return products_manager.get_categories(), 200

@bp_products.route("/all_products", methods=["GET"])
def all_products() -> tuple[dict[str, list[str]], int]:
    all_products: dict[str, dict[str, str]] = {}
    categories: list[str] = products_manager.get_categories()['categories']
    
    for i in categories:
        all_products[i] = products_manager.get_products(i)
    
    return all_products, 200
