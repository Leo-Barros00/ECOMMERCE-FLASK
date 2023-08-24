from flask import request, jsonify, abort
from app import app, db
from app.models import Product

@app.route("/products")
def get_all_products():
  products = Product.query.all()
  return jsonify([product.to_dict() for product in products])

@app.route('/products/<string:product_id>', methods=['GET'])
def get_product_by_id(product_id):
  product = Product.query.get(product_id)
  if product is None:
    abort(404) 
  return jsonify(product.to_dict())

@app.route("/products", methods=['POST'])
def product_post():
  data = request.json
  name = data['name']
  description = data['description']
  price = data['price']
  new_product = Product(name=name, description=description, price=price, stock_quantity=0)
  db.session.add(new_product)
  db.session.commit()
  return jsonify(new_product.to_dict()), 201

@app.route('/products/<string:product_id>', methods=['PUT'])
def update_product(product_id):
  product = Product.query.get(product_id)
  
  if product is None:
    abort(404)

  data = request.json
  if 'name' in data:
    product.name = data['name']
  if 'price' in data:
    product.price = data['price']
  if 'description' in data:
    product.description = data['description']
  if 'stock_quantity' in data:
    product.stock_quantity = data['stock_quantity']

  db.session.commit()
  
  return jsonify(product.to_dict()), 200

@app.route('/products/<string:product_id>', methods=['DELETE'])
def product_delete(product_id):
  product = Product.query.get(product_id)
  
  if product is None:
    abort(404)

  db.session.delete(product)
  db.session.commit()
  
  return '', 204