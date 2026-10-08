import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from app.routes.status import status_bp
from app.routes.sales_routes import sales_bp
from app.routes.sales_region_routes import sales_by_region_bp
from app.routes.product_routes import products_bp
from app.config.swagger import swagger_bp

load_dotenv()

app = Flask(__name__)


# Permitir consumo desde frontend y aplicaciones móviles
CORS(app)
app.json.ensure_ascii = False
app.json.sort_keys = False


# Registrar Blueprints
app.register_blueprint(status_bp)
app.register_blueprint(sales_bp)
app.register_blueprint(sales_by_region_bp)
app.register_blueprint(products_bp)
app.register_blueprint(swagger_bp)


if __name__ == "__main__":
    app.run(
        host=os.getenv("FLASK_HOST", "127.0.0.1"),
        port=5000,
        debug=os.getenv("FLASK_DEBUG", "false").lower() in {"1", "true", "yes"}
    )
