"""create attendance table

Revision ID: 7b2c4a6d9e10
Revises: 61648f19ad03
Create Date: 2026-10-28

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7b2c4a6d9e10'
down_revision: Union[str, None] = '61648f19ad03'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'attendance',
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('men', sa.Integer(), nullable=False),
        sa.Column('women', sa.Integer(), nullable=False),
        sa.Column('youth', sa.Integer(), nullable=False),
        sa.Column('children', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    op.drop_table('attendance')
