# database.py
import sqlite3
import logging


# Create a logger for the database module
logger = logging.getLogger(__name__)


# Database path
DATABASE_PATH = 'database/momo.db'


def connect_db():
    """
    Connects to the SQLite database and returns a connection and cursor.
    """
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        logger.error(f"Error connecting to database: {e}")
        raise


def close_db(conn):
    """
    Closes the database connection.
    """
    try:
        conn.close()
    except Exception as e:
        logger.error(f"Error closing database connection: {e}")
        raise


def create_database():
    """
    Creates the SQLite database and the Transactions table if they don't exist.
    """
    conn, cursor = connect_db()


    try:
        # Drop the table if it exists
        cursor.execute('DROP TABLE IF EXISTS Transactions')

