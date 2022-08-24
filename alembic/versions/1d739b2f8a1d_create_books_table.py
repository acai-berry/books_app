"""create books table

Revision ID: 1d739b2f8a1d
Revises:
Create Date: 2022-08-24 16:21:20.482467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1d739b2f8a1d"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("title", sa.String(256), index=True),
        sa.Column("author", sa.String(256), index=True),
        sa.Column("price", sa.Float),
    )


def downgrade() -> None:
    pass
