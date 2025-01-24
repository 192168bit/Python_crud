from core import ma

class CategoryResponseSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    name = ma.String(required=True)
    slug = ma.String(required=True)
    
class CategoryInsertSchema(ma.Schema):
    name = ma.String(required=True)
    slug = ma.String(required=True)
    is_active = ma.Boolean(required=True)
    parent_id = ma.Integer(allow_none=True)
    
class ProductInsertSchema(ma.Schema):
    pid = ma.String(dump_only=True)
    name = ma.String(required=True)
    slug = ma.String(required=True)
    description = ma.String()
    is_digital = ma.Boolean(required=True)
    created_at = ma.DateTime(required=True)
    is_active = ma.Boolean(required=True)
    stock_status = ma.Boolean(dump_only=True)
    category_id = ma.Integer()
    
class ProductLineInsertSchema(ma.Schema):
    price = ma.Decimal(places=2)
    sku = ma.String(dump_only=True)
    stock_qty = ma.Integer()
    is_active = ma.Boolean(required=True)
    order = ma.Integer()
    weight = ma.Float()
    created_at = ma.DateTime(dump_only=True)
    product_id = ma.Integer()
    
class ProductLineImageInsertSchema(ma.Schema):
    alternative_text = ma.String(max_length=200)
    url = ma.String()
    order = ma.Integer()
    product_line_id = ma.Integer()
    
class AttributeInsertSchema(ma.Schema):
    name = ma.String(required=True)
    description = ma.String()
    
class SeasonalInsertSchema(ma.Schema):
    start_date = ma.DateTime()
    end_date = ma.DateTime()
    name = ma.String(required=True)
    
class TypeInsertSchema(ma.Schema):
    name = ma.String()
    parent_id = ma.Integer(allow_none=True)

class AttributeValueInsertSchema(ma.Schema):
    attribute_value = ma.String(required=True)
    attribute_id = ma.Integer()
    
class ProductProdTypeInsertSchema(ma.Schema):
    product_id = ma.Integer()
    product_type_id = ma.Integer()
    
class ProductLineAttributeValue(ma.Schema):
    product_id = ma.Integer()
    product_type_id = ma.Integer()