from . import inventory_product_line_api_blueprint
from core.schema import ProductLineInsertSchema
from apifairy import response, body
from core.models import Product
from core import database

product_line_insert_schema = ProductLineInsertSchema()


@inventory_product_line_api_blueprint.route("/product-line", methods=["POST"])
@body(product_line_insert_schema)
@response(product_line_insert_schema)
def category_insert(kwargs):
    new_productline = Product(**kwargs)
    database.session.add(new_productline)
    database.session.commit()
    return new_productline