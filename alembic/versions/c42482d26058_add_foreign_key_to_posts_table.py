"""add foreign-key to posts table

Revision ID: c42482d26058
Revises: 1945c6722f87
Create Date: 2022-12-03 15:47:18.386032

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c42482d26058"
down_revision = "1945c6722f87"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "posts_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade():
    op.drop_constraint(
        "posts_users_fk",
        table_name="posts",
    )
    op.drop_column("posts", "owner_id")
    pass
