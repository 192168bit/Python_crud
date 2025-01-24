from . import inventory_product_api_blueprint
from core.schema import ProductInsertSchema
from apifairy import response, body
from core.models import Product
from core import database

product_insert_schema = ProductInsertSchema()


@inventory_product_api_blueprint.route("/product", methods=["POST"])
@body(product_insert_schema)
@response(product_insert_schema)
def category_insert(kwargs):
    new_product = Product(**kwargs)
    database.session.add(new_product)
    database.session.commit()
    return new_product