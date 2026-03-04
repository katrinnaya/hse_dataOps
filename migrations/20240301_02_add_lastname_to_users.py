"""
add lastname to users
"""

from yoyo import step

# Зависимость от первой миграции
__depends__ = {'20240301_01_create_users_table'}

steps = [
    step(
        """
        ALTER TABLE users 
        ADD COLUMN last_name VARCHAR(100)
        """,
        """
        ALTER TABLE users 
        DROP COLUMN last_name
        """
    )
]
