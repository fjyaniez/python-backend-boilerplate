"""create chatbot table

Revision ID: 188c9bc90464
Revises: 
Create Date: 2024-08-28 13:55:53.640408

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '188c9bc90464'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'chatbot',
        sa.Column('id', sa.Uuid, primary_key=True, default=sa.text('uuid_generate_v4()')),
        sa.Column('key', sa.String(256), nullable=False, unique=True, index=True),
        sa.Column('model', sa.String(1024), nullable=False),
        sa.Column('system_prompt', sa.Unicode(65536)),
    )


def downgrade() -> None:
    op.drop_table('chatbot')
