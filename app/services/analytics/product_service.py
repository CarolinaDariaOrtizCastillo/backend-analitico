from app.repositories.mongodb import product_repository
from app.repositories.sqlserver import sales_repository as sales_repo
from app.schemas.analytics_schema import IndicatorResponse


class ProductService:
    def __init__(self):
        self.sales_repository = sales_repo.SalesRepository()

    def get_top_product_month(self):
        sales_data = self.sales_repository.get_top_product()
        if not sales_data:
            return None

        product = product_repository.get_product_by_id(
            sales_data["product_id"]
        )
        if not product:
            return None

        return IndicatorResponse(
            indicator="top_product_month",
            title="Producto más vendido del mes",
            chart_type="card",
            data={
                "product_id": sales_data["product_id"],
                "product": product.get("name"),
                "category": product.get("category"),
                "quantity": sales_data["quantity"],
            },
            sources=["SQL Server", "MongoDB"],
        )
