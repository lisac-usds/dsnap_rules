"""empty message

Revision ID: 2684dcf3b305
Revises: 
Create Date: 2018-12-01 08:38:18.312300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2684dcf3b305'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('disaster',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('disaster_request_no', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('benefit_begin_date', sa.Date(), nullable=False),
    sa.Column('benefit_end_date', sa.Date(), nullable=False),
    sa.Column('state_or_territory', sa.String(length=2), nullable=False),
    sa.Column('worked_is_dsnap_eligible', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('disaster_request_no')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('disaster')
    # ### end Alembic commands ###
