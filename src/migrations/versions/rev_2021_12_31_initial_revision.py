"""Initial revision

Revision ID: 8ffb808f6ec4
Revises:
Create Date: 2021-12-31 12:21:46.261671

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "8ffb808f6ec4"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """Initial revision"""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "wine",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("winery", sa.String(length=64), nullable=True),
        sa.Column("variety", sa.String(length=64), nullable=True),
        sa.Column("year", sa.Integer(), nullable=True),
        sa.Column("attribute", sa.String(length=64), nullable=True),
        sa.Column("sugar", sa.String(length=64), nullable=True),
        sa.Column("count", sa.Integer(), server_default=sa.text("0"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "wine_add",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("wine_id", sa.Integer(), nullable=True),
        sa.Column("time", sa.DateTime(), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(
            ["wine_id"],
            ["wine.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "wine_remove",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("wine_id", sa.Integer(), nullable=True),
        sa.Column("time", sa.DateTime(), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(
            ["wine_id"],
            ["wine.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    """Initial revision (rollback)"""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("wine_remove")
    op.drop_table("wine_add")
    op.drop_table("wine")
    # ### end Alembic commands ###
