# ============================================================
#  utils/database.py – MySQL connection helpers
# ============================================================

import mysql.connector
from config import Config


def get_connection():
    """Return a new MySQL connection using settings from Config."""
    return mysql.connector.connect(
        host     = Config.DB_HOST,
        user     = Config.DB_USER,
        password = Config.DB_PASSWORD,
        database = Config.DB_NAME
    )


def execute_query(query: str, params: tuple = (), fetch: bool = False):
    """
    Run a parameterized query.

    Args:
        query  : SQL string with %s placeholders
        params : tuple of values to bind
        fetch  : True → return rows; False → commit & return lastrowid
    Returns:
        list[dict] when fetch=True, else int (lastrowid)
    """
    conn   = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(query, params)
        if fetch:
            result = cursor.fetchall()
            return result
        else:
            conn.commit()
            return cursor.lastrowid
    except mysql.connector.Error as err:
        conn.rollback()
        raise err
    finally:
        cursor.close()
        conn.close()
