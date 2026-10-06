from app.repositories.sqlserver.sales_region import SalesRegionRepository
from app.schemas.analytics_schema import IndicatorResponse


class SalesRegionService:


    def __init__(self):
        self.repository = SalesRegionRepository()


    def sales_by_region(self):
        result = self.repository.get_sales_region()
        return IndicatorResponse(
            indicator="sales_by_region",
            title="Ventas por Región",
            chart_type="bar",
            data=result,
            sources=[
                "SQL Server"
            ]
        )
