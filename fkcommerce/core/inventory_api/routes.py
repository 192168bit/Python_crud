from . import inventory_category_api_blueprint


@inventory_category_api_blueprint.route('/category', methods=['GET'])
def category():
    pass