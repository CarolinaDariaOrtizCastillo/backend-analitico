from app.database.sqlserver import get_sqlserver_connection


class SalesRegionRepository:
    def get_sales_region(self):
        connection = get_sqlserver_connection()
        try:
            cursor = connection.cursor()
            query = """
            SELECT
                region,
                SUM(total_amount) AS sales
            FROM sales
            GROUP BY region
            ORDER BY sales DESC;
            """
            cursor.execute(query)
            rows = cursor.fetchall()
        finally:
            connection.close()

        return [
            {
                "region": row[0],
                "sales": float(row[1])
            }
            for row in rows
        ]
