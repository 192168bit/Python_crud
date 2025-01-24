from . import inventory_attribute_api_blueprint
from core.schema import AttributeInsertSchema
from apifairy import response, body
from core.models import Attribute
from core import database

attribute_insert_schema = AttributeInsertSchema()


@inventory_attribute_api_blueprint.route("/attribute", methods=["POST"])
@body(attribute_insert_schema)
@response(attribute_insert_schema)
def attribute_insert(kwargs):
    new_attribute = Attribute(**kwargs)
    database.session.add(new_attribute)
    database.session.commit()
    return new_attribute