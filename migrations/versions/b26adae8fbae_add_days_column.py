"""add days column

Revision ID: b26adae8fbae
Revises: 2d5d5152de2e
Create Date: 2021-07-22 23:39:28.105752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b26adae8fbae'
down_revision = '2d5d5152de2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('travelposts', sa.Column('days', sa.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('travelposts', 'days')
    # ### end Alembic commands ###