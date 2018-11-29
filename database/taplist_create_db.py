import sqlite3
from sqlite3 import Error

bar_table = """CREATE TABLE bar (bar_id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                hood TEXT NOT NULL);"""
brewery_table = """CREATE TABLE brewery (brewery_id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL,
                                        city TEXT NOT NULL);"""
beer_table = """CREATE TABLE beer (beer_id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                type TEXT, alc TEXT,
                                brewery_id INTEGER,
                                FOREIGN KEY (brewery_id) REFERENCES brewery (brewery_id));"""
taplist_table = """CREATE TABLE taplist (taplist_id INTEGER PRIMARY KEY,
                                        bar_id INTEGER,
                                        beer_id INTEGER,
                                        FOREIGN KEY (bar_id) REFERENCES bar (bar_id),
                                        FOREIGN KEY (beer_id) REFERENCES beer (beer_id));"""


def create_tables(conn):1
    try:
        c = conn.cursor()
        c.execute(bar_table)
        c.execute(brewery_table)
        c.execute(beer_table)
        c.execute(taplist_table)
    except Error as e:
        print(e)


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        create_tables(conn);
    except Error as e:
        print(e)
    finally:
        conn.close()


if __name__ == '__main__':
    create_connection("taplist_db.sqlite")
