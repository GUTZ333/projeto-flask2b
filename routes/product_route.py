from flask import Blueprint, request
from controllers.products_controller import create_product

product_routes = Blueprint("product_routes", __name__)

@product_routes.route("/create-product", methods=["POST"])
def create_products_post():
  data = request.json
  return create_product(data)

