"""empty message

Revision ID: e3f9a9f2c823
Revises: e19fb4b3c2c2
Create Date: 2016-02-09 16:55:08.071037

"""

# revision identifiers, used by Alembic.
revision = 'e3f9a9f2c823'
down_revision = 'e19fb4b3c2c2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('t_gdg_help_desk', sa.Column('author_tel', sa.String(length=15), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('t_gdg_help_desk', 'author_tel')
    ### end Alembic commands ###
