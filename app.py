from flask import Flask
from db import db
from routes.product_route import product_routes

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

app.register_blueprint(product_routes)

if __name__ == "__main__":
  with app.app_context():
    db.create_all()
  app.run(debug=True)