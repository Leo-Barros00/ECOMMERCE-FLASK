from flask import Flask
import os
import importlib

app = Flask(__name__)

@app.route("/health")
def hello_world():
    return {'status': 'Running' }

# importing all routes from routes directory
route_folder = os.path.join(os.path.dirname(__file__), 'routes')
for filename in os.listdir(route_folder):
    if filename.endswith('.py') and filename != '__init__.py':
        module_name = f"app.routes.{filename[:-3]}"
        importlib.import_module(module_name)