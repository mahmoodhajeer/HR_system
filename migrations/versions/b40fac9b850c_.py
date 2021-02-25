"""empty message

Revision ID: b40fac9b850c
Revises: 
Create Date: 2021-02-24 12:10:10.605110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b40fac9b850c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('candidate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=30), nullable=False),
    sa.Column('date_of_birth', sa.String(length=10), nullable=False),
    sa.Column('years_of_experience', sa.String(length=2), nullable=True),
    sa.Column('department_ID', sa.String(length=7), nullable=False),
    sa.Column('resume', sa.String(length=10), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('years_of_experience')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('candidate')
    # ### end Alembic commands ###
