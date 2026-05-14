"""initial schema

Revision ID: 0001_initial
Revises: 
Create Date: 2026-05-14
"""
from alembic import op
import sqlalchemy as sa

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("username", sa.String(length=100), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("created_at", sa.DateTime(), nullable=False),
    )
    op.create_index("ix_users_username", "users", ["username"], unique=True)

    op.create_table(
        "alerts",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("rule_name", sa.String(length=255), nullable=False),
        sa.Column("severity", sa.String(length=50), nullable=False),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("payload", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
    )
    op.create_index("ix_alerts_rule_name", "alerts", ["rule_name"], unique=False)

    op.create_table(
        "incidents",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("severity", sa.String(length=50), nullable=False),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("alert_id", sa.Integer(), sa.ForeignKey("alerts.id"), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
    )

    op.create_table(
        "playbook_runs",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("playbook_name", sa.String(length=255), nullable=False),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("trigger_type", sa.String(length=100), nullable=False),
        sa.Column("trigger_ref_id", sa.String(length=255), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
    )
    op.create_index("ix_playbook_runs_playbook_name", "playbook_runs", ["playbook_name"], unique=False)

    op.create_table(
        "playbook_steps",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("run_id", sa.Integer(), sa.ForeignKey("playbook_runs.id"), nullable=False),
        sa.Column("step_id", sa.String(length=120), nullable=False),
        sa.Column("action", sa.String(length=255), nullable=False),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("input_payload", sa.JSON(), nullable=False),
        sa.Column("output_payload", sa.JSON(), nullable=False),
        sa.Column("error", sa.String(length=500), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
    )
    op.create_index("ix_playbook_steps_run_id", "playbook_steps", ["run_id"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_playbook_steps_run_id", table_name="playbook_steps")
    op.drop_table("playbook_steps")
    op.drop_index("ix_playbook_runs_playbook_name", table_name="playbook_runs")
    op.drop_table("playbook_runs")
    op.drop_table("incidents")
    op.drop_index("ix_alerts_rule_name", table_name="alerts")
    op.drop_table("alerts")
    op.drop_index("ix_users_username", table_name="users")
    op.drop_table("users")
