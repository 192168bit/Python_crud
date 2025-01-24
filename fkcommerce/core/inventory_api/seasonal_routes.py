from . import inventory_seasonal_api_blueprint
from core.schema import SeasonalInsertSchema
from apifairy import response, body
from core.models import SeasonalEvent
from core import database

seasonal_insert_schema = SeasonalInsertSchema()


@inventory_seasonal_api_blueprint.route("/seasonal", methods=["POST"])
@body(seasonal_insert_schema)
@response(seasonal_insert_schema)
def seasonal_insert(kwargs):
    new_event = SeasonalEvent(**kwargs)
    database.session.add(new_event)
    database.session.commit()
    return new_event