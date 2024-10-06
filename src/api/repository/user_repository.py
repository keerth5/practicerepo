from src.api.config.__init__ import settings
import psycopg2

# class UserRepository:
    # def __init__(self, db):
    #     """
    #     Initialize a UserRepository instance.

    #     Args:
    #         db: A callable that returns a database connection.
    #     """
    #     self.db = db

def get_db_connection():
    """
    Establishes a connection to the database, using the DATABASE_URL environment
    variable or the default setting for the current environment.

    Yields a psycopg2 connection object.
    """
    with psycopg2.connect(settings.DATABASE_URL) as conn:
        yield conn

def check_db_connection():
    """
    Attempts to establish a connection to the database and execute a simple
    query.

    Returns a string indicating the outcome of the check. If the check
    succeeds, the string will be "Connected". If the check fails, the
    string will be a description of the error that occurred.

    :return: A string indicating the health of the database connection.
    :rtype: str
    """
    try:
        with get_db_connection.cursor() as cur:
            cur.execute("SELECT 1")
        return "Connected"
    except Exception as e:
        return f"Failed to connect to database: {e}"
