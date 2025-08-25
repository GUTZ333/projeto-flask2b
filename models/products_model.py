from db import db

class Product(db.Model):
  __tablename__ = "products"

  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(80), nullable=False)
  categoria = db.Column(db.String(80), nullable=False)
  preco = db.Column(db.Integer, nullable=False)

  def json(self):
    return {
      "id": self.id,
      "categoria": self.categoria,
      "nome": self.nome,
      "preco": self.preco,
    }