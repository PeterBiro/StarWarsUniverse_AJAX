import psycopg2
from private_settings import connection_constants


def check_user(user_name):
    try:
        host, dbname, user, password = connection_constants()
        connect_str = "dbname='{}' user='{}' host='{}' password='{}'".format(dbname, user, host, password)
        connection = psycopg2.connect(connect_str)
        cursor = connection.cursor()
        connection.autocommit = True
        cursor = connection.cursor()
        query = ""###
        cursor.execute(query)


    except psycopg2.DatabaseError as exception:
        print(exception)
        rows = exception

    finally:
        if connection:
            connection.close()
    return rows


if __name__ == '__main__':
    pass
