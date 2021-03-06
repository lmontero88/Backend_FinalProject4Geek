"""empty message

Revision ID: 0d697c545a40
Revises: 
Create Date: 2020-12-08 15:14:32.690970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d697c545a40'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Favourite_Product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Favourite_User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sport',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('registered_at', sa.DateTime(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('password_hash', sa.String(length=100), nullable=False),
    sa.Column('birthdate', sa.DateTime(), nullable=True),
    sa.Column('phones', sa.String(length=100), nullable=True),
    sa.Column('gender', sa.String(length=100), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('photo', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('Match',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_to_id', sa.Integer(), nullable=True),
    sa.Column('user_from_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_from_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_to_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('User_Sport',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('experiencia', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('sport_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['sport_id'], ['sport.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id', 'user_id', 'sport_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('User_Sport')
    op.drop_table('Match')
    op.drop_table('user')
    op.drop_table('sport')
    op.drop_table('role')
    op.drop_table('Favourite_User')
    op.drop_table('Favourite_Product')
    # ### end Alembic commands ###
