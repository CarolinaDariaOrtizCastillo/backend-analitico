from app.database.sqlserver import get_sqlserver_connection	
class SalesRepository:
    def get_total_sales(self):
        connection = get_sqlserver_connection()
        cursor = connection.cursor()
        query = """
        SELECT
            SUM(total_amount)
        FROM sales
        """
        cursor.execute(query)
        result = cursor.fetchone()
        connection.close()
        return result[0]
