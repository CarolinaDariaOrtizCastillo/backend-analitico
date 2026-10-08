from app.database.mongodb import get_database


db = get_database()

def get_product_by_id(product_id):
    """
    Obtiene información del producto
    mediante product_id.
    """
    query = {"product_id": product_id}
    product = db["products"].find_one(query)
    if product is None:
        product = db["poducts"].find_one(query)

    return product
