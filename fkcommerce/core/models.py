import uuid

from core import database as db

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import (Column, Integer, String, Boolean, ForeignKey, text, Text, DateTime, DECIMAL, Float)

class Category(db.Model):
    __tablename__ = "category"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    slug = Column(String(200), unique=True, nullable=False)
    is_active = Column(Boolean, default=False)
    parent_id = Column(Integer, ForeignKey("category.id"), nullable=True)
    
    def __repr__(self):
        return f"<Name: {self.name}>"
    
class Product(db.Model):
    __tablename__ = "product"
    
    id = Column(Integer, primary_key=True)
    pid = Column(UUID(as_uuid=True), unique=True, nullable=False, server_default=text("uuid_generate_v4()"))
    name = Column(String(200), unique=True, nullable=False)
    slug = Column(String(255), unique=True, nullable=False)
    description = Column(Text)
    is_digital = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=db.text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=db.text("CURRENT_TIMESTAMP"), onupdate=db.func.now())
    is_active = Column(Boolean, default=False)
    stock_status = Column(String(100), default="OUT_OF_STOCK")
    category_id = Column(Integer, ForeignKey("category.id"))
    seasonal_event = Column(Integer, ForeignKey("seasonal_event.id"), nullable=True)
    
    def __repr__(self):
        return f"<Name: {self.name}>"
    
class ProductLine(db.Model):
    __tablename__ = "product_line"
    
    id = Column(Integer, primary_key=True)
    price = Column(DECIMAL(5,2))
    sku = Column(UUID(as_uuid=True), default=uuid.uuid4)
    stock_qty = Column(Integer, default=0)
    is_active = Column(Boolean, default=False)
    order = Column(Integer)
    weight = Column(Float)
    created_at = Column(DateTime, server_default=db.text("CURRENT_TIMESTAMP"))
    product_id = Column(Integer, ForeignKey("product.id"))

    def __repr__(self):
        return f"ProductLine {self.id}"

class ProductImage(db.Model):
    __tablename__ = "product_image"
    
    id = Column(Integer, primary_key=True)
    alternative_text = Column(String(200))
    url = Column(String)
    order = Column(Integer)
    product_line_id = Column(Integer, ForeignKey("product_line.id"))
    
    def __repr__(self):
        return f"ProductImage {self.id}"

class SeasonalEvent(db.Model):
    __tablename__ = "seasonal_event"
    
    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    name = Column(String(100), unique=True)
    
    def __repr__(self):
        return self.name
    
class Attribute(db.Model):
    __tablename__ = "attribute"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    description = Column(Text)
    
    def __repr__(self):
        return self.name

class AttributeValue(db.Model):
    __tablename__ = "attribute_value"
    
    id = Column(Integer, primary_key=True)
    attribute_value = Column(String(100))
    attribute_id = Column(Integer, ForeignKey("attribute.id"))
    
    def __repr__(self):
        return self.attribute_value
    
class ProductType(db.Model):
    __tablename__ = "product_type"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    parent_id = Column(Integer, ForeignKey("product_type.id"))
    
    def __repr__(self):
        return self.name

class Product_ProductType(db.Model):
    __tablename__ = "product_product_type"
    
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    product_type_id = Column(Integer, ForeignKey("product_type.id"))
    

class ProductLine_AttributeValue(db.Model):
    __tablename__ = "product_line_attribute_value"
    
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("attribute_value.id"))
    product_type_id = Column(Integer, ForeignKey("product_line.id"))
