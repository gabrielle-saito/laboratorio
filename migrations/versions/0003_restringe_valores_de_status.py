"""restringe valores de status

Revision ID: 0003
Revises: ed320ea2db8c
Create Date: 2026-10-08 13:46:31.775138
"""
from alembic import op
import sqlalchemy as sa


revision = '0003'
down_revision = 'ed320ea2db8c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_check_constraint(
        "ck_arquivos_status", "arquivos", "status IN ('pendente', 'concluido')"
    )


def downgrade():
    op.drop_constraint("ck_arquivos_status", "arquivos", type_="check")
