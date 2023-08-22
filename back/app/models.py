from app import db
import uuid

class Product(db.Model):
  id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
  name = db.Column(db.String(80), nullable=False)
  description = db.Column(db.Text, nullable=True)
  price = db.Column(db.Float, nullable=False)
  image_url = db.Column(db.String(200), nullable=True)
  stock_quantity = db.Column(db.Integer, nullable=False)

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'description': self.description,
      'price': self.price,
      'image_url': self.image_url,
      'stock_quantity': self.stock_quantity
    }