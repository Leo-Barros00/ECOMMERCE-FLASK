from flask import abort, jsonify, request
from app import app, db
from app.models import Category, Product

@app.route("/categories")
def get_all_categories():
  categories = Category.query.all()
  return jsonify([category.to_dict() for category in categories])

@app.route("/categories", methods=['POST'])
def category_post():
  data = request.json
  name = data['name']
  new_category = Category(name=name)
  db.session.add(new_category)
  db.session.commit()
  return jsonify(new_category.to_dict()), 201

@app.route("/categories/<string:category_id>", methods=['PUT'])
def category_put(category_id):
  category = Category.query.get(category_id)
  
  if category is None:
    abort(404)

  data = request.json
  name = data['name']
  new_category = Category(name=name)
  db.session.add(new_category)
  db.session.commit()
  return jsonify(new_category.to_dict()), 201

