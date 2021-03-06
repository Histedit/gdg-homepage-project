"""empty message

Revision ID: bef45169c904
Revises: f1318346a431
Create Date: 2016-01-30 16:53:34.058084

"""

# revision identifiers, used by Alembic.
revision = 'bef45169c904'
down_revision = 'f1318346a431'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.String(length=30), nullable=True),
    sa.Column('user_pw', sa.String(length=255), nullable=True),
    sa.Column('permission', sa.SMALLINT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('t_gdg_help_desk')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_gdg_help_desk',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('date_created', mysql.DATETIME(), nullable=True),
    sa.Column('date_modified', mysql.DATETIME(), nullable=True),
    sa.Column('help_title', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('help_content', mysql.TEXT(), nullable=True),
    sa.Column('author_address', mysql.VARCHAR(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('user_table')
    ### end Alembic commands ###
