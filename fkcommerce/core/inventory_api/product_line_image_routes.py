from . import inventory_product_line_image_api_blueprint
from core.schema import ProductLineImageInsertSchema
from apifairy import response, body
from core.models import ProductImage
from core import database

product_line_image_insert_schema = ProductLineImageInsertSchema()


@inventory_product_line_image_api_blueprint.route("/product-line-image", methods=["POST"])
@body(product_line_image_insert_schema)
@response(product_line_image_insert_schema)
def category_insert(kwargs):
    new_productline_image = ProductImage(**kwargs)
    database.session.add(new_productline_image)
    database.session.commit()
    return new_productline_image