from flask import request, jsonify, abort
from app import app, db
from app.models import Order, OrderProducts, Product
import os

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
  data = request.form
  name = data['name']
  description = data['description']
  price = data['price']
  category_id = data['category_id']
  stock_quantity = data['stock_quantity']

  new_product = Product(name=name, description=description, price=price, stock_quantity=stock_quantity, category_id=category_id)

  db.session.add(new_product)
  db.session.commit()
  image_file = request.files['image']
  if image_file.filename == '':
    return "No selected image", 400
  
  _, file_extension = os.path.splitext(image_file.filename)

  new_filename = new_product.id + file_extension
  image_file.save('./app/static/' + new_filename)

  new_product.image_url = '/static/' + new_filename
  db.session.commit()

  return jsonify(new_product.to_dict()), 201

@app.route("/products/order", methods=['POST'])
def product_order_post():
  data = request.json
  address = data['address']  
  status = data['status']  

  if 'products' in data and isinstance(data['products'], list):
    products = data['products']
  else:
    return "Invalid list of products", 400

  for prod in products:
    new_order = Order(status=status, address=address)
    db.session.add(new_order)
    db.session.commit()
    association = OrderProducts.insert().values(product_id=prod['id'], order_id=new_order.id, quantity=prod['quantity'])
    db.session.execute(association)
    db.session.commit()

  
  return '', 201

@app.route('/products/<string:product_id>', methods=['PUT'])
def update_product(product_id):
  product = Product.query.get(product_id)
  
  if product is None:
    abort(404)

  data = request.form
  if 'name' in data:
    product.name = data['name']
  if 'price' in data:
    product.price = data['price']
  if 'description' in data:
    product.description = data['description']
  if 'stock_quantity' in data:
    product.stock_quantity = data['stock_quantity']
  if 'category_id' in data:
    product.category_id = data['category_id']

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