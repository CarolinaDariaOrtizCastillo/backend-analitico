from flask import Blueprint, jsonify
from app.services.analytics.sales_region import SalesRegionService

sales_by_region_bp = Blueprint(
    "sales_by_region",
    __name__
)

region_service = SalesRegionService()


@sales_by_region_bp.route(
    "/analytics/sales-by-region",
    methods=["GET"]
)
def get_sales_by_region():
    result = region_service.sales_by_region()
    return jsonify(
        result.__dict__
    )

