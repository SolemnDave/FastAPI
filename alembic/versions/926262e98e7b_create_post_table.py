"""create post table

Revision ID: 926262e98e7b
Revises: 
Create Date: 2022-12-03 15:17:56.931142

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "926262e98e7b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_table("posts")
    pass
