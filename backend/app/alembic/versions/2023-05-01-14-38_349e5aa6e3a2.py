"""empty message

Revision ID: 349e5aa6e3a2
Revises: d345e1cac250
Create Date: 2023-05-01 14:38:23.045521

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlmodel # added


# revision identifiers, used by Alembic.
revision = '349e5aa6e3a2'
down_revision = 'd345e1cac250'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm") 
    op.alter_column('User', 'first_name', nullable=False, new_column_name='name')
    op.drop_column('User', 'last_name')
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
