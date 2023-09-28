import os
import importlib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.database.utils import getDataBaseConnectionString

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = getDataBaseConnectionString()

db = SQLAlchemy(app)

@app.route("/health")
def hello_world():
    return {'status': 'Running' }

# importing all routes from routes directory
route_folder = os.path.join(os.path.dirname(__file__), 'routes')
for filename in os.listdir(route_folder):
    if filename.endswith('.py') and filename != '__init__.py':
        module_name = f"app.routes.{filename[:-3]}"
        importlib.import_module(module_name)