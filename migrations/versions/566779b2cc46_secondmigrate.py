"""secondmigrate

Revision ID: 566779b2cc46
Revises: 
Create Date: 2021-01-27 16:52:41.225121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '566779b2cc46'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=40), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###