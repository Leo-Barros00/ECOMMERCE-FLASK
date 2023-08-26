from flask import request, jsonify, abort
from app import app, db
from app.models import Order

@app.route("/orders")
def get_all_orders():
  orders = Order.query.all()
  return jsonify([order.to_dict() for order in orders])

@app.route('/oders/<string:oder_id>', methods=['GET'])
def get_order_by_id(order_id):
  order = Order.query.get(order)
  if order is None:
    abort(404) 
  return jsonify(order.to_dict())

@app.route("/orders", methods=['POST'])
def order_post():
  data = request.json
  name = data['name']
  address = data['address']  
  order_id = data['order_id']
  new_order = Order(name=name, address=address, order_id=order_id)
  db.session.add(new_order)
  db.session.commit()
  return jsonify(new_order.to_dict()), 201

@app.route('/orders/<string:order_id>', methods=['PUT'])
def update_order(order_id):
  order = Order.query.get(order_id)
  
  if order is None:
    abort(404)

  data = request.json
  if 'name' in data:
    order.name = data['name']
  if 'address' in data:
    order.price = data['address']

  db.session.commit()
  
  return jsonify(order.to_dict()), 200

@app.route('/orders/<string:order_id>', methods=['DELETE'])
def order_delete(order_id):
  order = Order.query.get(order_id)
  
  if order is None:
    abort(404)

  db.session.delete(order)
  db.session.commit()
  
  return '', 204