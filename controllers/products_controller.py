from models.products_model import Product
from db import db
from flask import make_response
import json 

def create_product(product):
  new_product = Product(
    nome=product["nome"],
    categoria=product["categoria"],
    preco=product["preco"],
  )
  db.session.add(new_product)
  db.session.commit()
  response = make_response(
    json.dumps({
      "message": "Register product successfully!!",
      "product": new_product.json()
    }, sort_keys=False)
  )
  response.headers['content-Type'] = 'application/json'
  return response