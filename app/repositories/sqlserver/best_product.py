from app.database.sqlserver import get_sqlserver_connection	

class BestProductRepository:
    def get_top_product(self):
        connection = get_sqlserver_connection()
        try:
            cursor = connection.cursor()
            query = """
            SELECT TOP 1
                product_id,
                SUM(quantity) AS total_quantity
            FROM sales_detail
            GROUP BY product_id
            ORDER BY total_quantity DESC
            """
            cursor.execute(query)
            result = cursor.fetchone()
        finally:
            connection.close()

        if result:
            return {
                "product_id": result[0],
                "quantity": result[1]
            }
        return None

