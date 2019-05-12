import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def select_all_telephones(conn):
    """
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM telephones")
    rows = cur.fetchall()
    return rows


def create_telephone(conn, telephone):
    """
    Create a new project into the telephone table
    :param conn:
    :param telephone:
    :return: telephone id
    """
    sql = ''' INSERT INTO telephones(number)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, (telephone,))
    return cur.lastrowid


def main():
    database = "telephones.db"

    sql_create_phones_table = """ CREATE TABLE IF NOT EXISTS telephones (
                                        id integer PRIMARY KEY,
                                        number text NOT NULL
                                    ); """

    # create a database connection
    conn = create_connection(database)

    if conn is not None:
        # create phones table
        create_table(conn, sql_create_phones_table)
    else:
        print("Error! cannot create the database connection.")

    print(select_all_telephones(conn))


if __name__ == '__main__':
    main()



# all_telephones = [
#     '380639176241',
#     '380671274401',
#     '380671274403',
#     '380672832500',
#     '380673174409',
#     '380675054410',
#     '380675414406',
#     '380675554402',
#     '380675617440',
#     '380675674432',
#     '380675982707',
#     '380678744408',
#     '380679514404',
#     '380930124912',
#     '380936488090',
#     '380983567721',
#     '380991231231',
# ]
#
# for t in all_telephones:
#     # create telephone
#     create_telephone(conn, t)
# conn.commit()
