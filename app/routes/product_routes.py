from flask import Blueprint, jsonify
from pymongo.errors import PyMongoError

try:
    from app.services.analytics.product_service import ProductService
except ModuleNotFoundError:
    from services.analytics.product_service import ProductService

product_service = ProductService()

products_bp = Blueprint(
    "products",
    __name__
)

@products_bp.route(
    "/analytics/top-product",
    methods=["GET"]
)
def top_product_month():
    try:
        result = product_service.get_top_product_month()
    except PyMongoError:
        return jsonify({
            "message": "No se pudo conectar con MongoDB Atlas. Verifica la conectividad TLS y la IP autorizada en Network Access."
        }), 503

    if not result:
        return jsonify({
            "message":
            "No se encontró información"
        }),404
    return jsonify(
        result.__dict__
    )
