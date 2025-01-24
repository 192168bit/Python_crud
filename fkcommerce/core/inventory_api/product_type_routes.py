from . import inventory_type_api_blueprint
from core.schema import TypeInsertSchema
from apifairy import response, body
from core.models import ProductType
from core import database

type_insert_schema = TypeInsertSchema()


@inventory_type_api_blueprint.route("/type", methods=["POST"])
@body(type_insert_schema)
@response(type_insert_schema)
def attribute_insert(kwargs):
    new_type = ProductType(**kwargs)
    database.session.add(new_type)
    database.session.commit()
    return new_type