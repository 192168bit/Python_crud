from . import inventory_attribute_value_api_blueprint
from core.schema import AttributeValueInsertSchema
from apifairy import response, body
from core.models import AttributeValue
from core import database

attribute_insert_schema = AttributeValueInsertSchema()


@inventory_attribute_value_api_blueprint.route("/attribute-value", methods=["POST"])
@body(attribute_insert_schema)
@response(attribute_insert_schema)
def attribute_value_insert(kwargs):
    attr_value = AttributeValue(**kwargs)
    database.session.add(attr_value)
    database.session.commit()
    return attr_value