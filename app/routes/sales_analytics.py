from flask import Blueprint, jsonify
from app.services.analytics.sales_service import SalesService

analytics_bp = Blueprint(
    "analytics",
    __name__
)

service = SalesService()


@analytics_bp.route(
    "/analytics/sales-total",
    methods=["GET"]
)
def sales_total():
    result = service.total_sales()
    return jsonify(result.__dict__)
