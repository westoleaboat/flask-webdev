"""empty message

Revision ID: 252a07cbafe5
Revises: 1e1e62d5d6d8
Create Date: 2022-12-28 22:51:20.753920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '252a07cbafe5'
down_revision = '1e1e62d5d6d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # with op.batch_alter_table('items', schema=None) as batch_op:
    #     batch_op.alter_column('price',
    #            existing_type=sa.REAL(),
    #            type_=sa.Float(precision=2),
    #            existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # with op.batch_alter_table('items', schema=None) as batch_op:
    #     batch_op.alter_column('price',
    #            existing_type=sa.Float(precision=2),
    #            type_=sa.REAL(),
    #            existing_nullable=False)

    # ### end Alembic commands ###