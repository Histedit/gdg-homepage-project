"""empty message

Revision ID: c198929399c2
Revises: b0a2de758473
Create Date: 2016-02-21 16:11:39.966983

"""

# revision identifiers, used by Alembic.
revision = 'c198929399c2'
down_revision = 'b0a2de758473'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=10), nullable=True),
    sa.Column('picture', sa.String(length=255), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('user_num', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_num'], ['user_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('portfolio', sa.Column('picture', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('portfolio', 'picture')
    op.drop_table('user_profile')
    ### end Alembic commands ###
