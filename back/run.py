from app import app, db
from app.models import Product

with app.app_context():
  db.create_all()
  app.run(port=8000, debug=True)