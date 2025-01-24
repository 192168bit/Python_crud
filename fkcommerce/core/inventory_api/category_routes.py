from . import inventory_category_api_blueprint
from core.schema import CategoryResponseSchema, CategoryInsertSchema
from apifairy import response, body
from core.models import Category
from core import database

category_response_schema = CategoryResponseSchema(many=True)
category_insert_schema = CategoryInsertSchema()

@inventory_category_api_blueprint.route("/category", methods=["GET"])
@response(category_response_schema)
def category():
    return Category.query.all()

@inventory_category_api_blueprint.route("/category", methods=["POST"])
@body(category_insert_schema)
@response(category_insert_schema)
def category_insert(kwargs):
    new_category = Category(**kwargs)
    database.session.add(new_category)
    database.session.commit()
    return new_category