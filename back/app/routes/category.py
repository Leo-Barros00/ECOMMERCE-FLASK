from flask import abort, jsonify, request
from sqlalchemy import func
from app import app, db
from app.models import Category, Product
from app.utils.string import slugify

@app.route("/categories")
def get_all_categories():
  category_results = db.session.query(Category, func.count(Product.id).label('product_count')) \
      .outerjoin(Product) \
      .group_by(Category.id) \
      .all()

  return [{**category.to_dict(), 'productCount': product_count} for category, product_count in category_results]

@app.route('/categories/<string:category_id>', methods=['GET'])
def get_category_by_id(category_id):
  category, product_count = (db.session.query(Category, func.count(Product.id).label('product_count'))
    .outerjoin(Product)
    .filter(Category.id == category_id)
    .group_by(Category.id)
    .first() or (None, 0))
    
  if not category:
    abort(404)

  return {**category.to_dict(), 'productCount': product_count}

@app.route('/categories/slug/<string:slug>', methods=['GET'])
def get_category_by_slug(slug):
  # category, product_count = (db.session.query(Category, func.count(Product.id).label('product_count'))
  #   .outerjoin(Product)
  #   .filter(Category.slug == slug)
  #   .group_by(Category.id)
  #   .first() or (None, 0))
    
  # if not category:
  #   abort(404)

  # return {**category.to_dict(), 'productCount': product_count}
  category = Category.query.filter_by(slug=slug).first_or_404()

  # Converta a categoria e seus produtos para dicionários
  category_dict = category.to_dict()
  category_dict['products'] = [product.to_dict() for product in category.products]

  return jsonify(category_dict)

@app.route("/categories", methods=['POST'])
def category_post():
  data = request.json
  name = data['name']
  slug = slugify(name)
  new_category = Category(name=name, slug=slug)
  db.session.add(new_category)
  db.session.commit()
  return jsonify(new_category.to_dict()), 201

@app.route("/categories/<string:category_id>", methods=['PUT'])
def category_put(category_id):
  category = Category.query.get(category_id)
  
  if category is None:
    abort(404)

  data = request.json
  if 'name' in data:
    category.name = data['name']
    category.slug = slugify(data['name'])
  
  db.session.commit()
  return jsonify(category.to_dict()), 201

@app.route("/categories/<string:category_id>", methods=['DELETE'])
def category_delete(category_id):
  category = Category.query.get(category_id)
  
  if category is None:
    abort(404)

  db.session.delete(category)
  db.session.commit()
  
  return '', 204

