"""initial migration

Revision ID: 1d0944cfc500
Revises: 
Create Date: 2025-01-23 18:11:07.391491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d0944cfc500'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attribute',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('slug', sa.String(length=200), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('product_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['product_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('seasonal_event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('attribute_value',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('attribute_value', sa.String(length=100), nullable=True),
    sa.Column('attribute_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['attribute_id'], ['attribute.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pid', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('slug', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('is_digital', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('stock_status', sa.String(length=100), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('seasonal_event', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['seasonal_event'], ['seasonal_event.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('pid'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('product_line',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.DECIMAL(precision=5, scale=2), nullable=True),
    sa.Column('sku', sa.UUID(), nullable=True),
    sa.Column('stock_qty', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_product_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('product_type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['product_type_id'], ['product_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('alternative_text', sa.String(length=200), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('product_line', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_line'], ['product_line.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_line_attribute_value',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('product_type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['attribute_value.id'], ),
    sa.ForeignKeyConstraint(['product_type_id'], ['product_line.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_line_attribute_value')
    op.drop_table('product_image')
    op.drop_table('product_product_type')
    op.drop_table('product_line')
    op.drop_table('product')
    op.drop_table('attribute_value')
    op.drop_table('seasonal_event')
    op.drop_table('product_type')
    op.drop_table('category')
    op.drop_table('attribute')
    # ### end Alembic commands ###
