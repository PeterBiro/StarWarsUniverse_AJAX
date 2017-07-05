import psycopg2
# from private_settings import connection_constants


def check_user(user_name):
    try:
        # host, dbname, user, password = connection_constants()
        # connect_str = "dbname='{}' user='{}' host='{}' password='{}'".format(dbname, user, host, password)
	# connection = psycopg2.connect(connect_str)
	
	urllib.parse.uses_netloc.append('postgres')
	url = urllib.parse.urlparse(os.environ.get('DATABASE_URL'))
	connection = psycopg2.connect(
    		database=url.path[1:],
    		user=url.username,
    		password=url.password,
    		host=url.hostname,
    		port=url.port
	)

        cursor = connection.cursor()
        connection.autocommit = True
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username ='{}';".format(user_name)
        cursor.execute(query)
        if len(cursor.fetchall()) == 0:
            result = "OK"
        else:
            result = "not OK"
    except psycopg2.DatabaseError as exception:
        print(exception)
    finally:
        if connection:
            connection.close()
    return result


def new_user(username, passw):
    try:
        # host, dbname, user, password = connection_constants()
        # connect_str = "dbname='{}' user='{}' host='{}' password='{}'".format(dbname, user, host, password)
	# connection = psycopg2.connect(connect_str)
	
	urllib.parse.uses_netloc.append('postgres')
	url = urllib.parse.urlparse(os.environ.get('DATABASE_URL'))
	connection = psycopg2.connect(
    		database=url.path[1:],
    		user=url.username,
    		password=url.password,
    		host=url.hostname,
    		port=url.port
	)

        cursor = connection.cursor()
        connection.autocommit = True
        cursor = connection.cursor()
        query = "INSERT INTO users (username, password) VALUES ('{}','{}');".format(username, passw)
        cursor.execute(query)
    except psycopg2.DatabaseError as exception:
        print(exception)
    finally:
        if connection:
            connection.close()


def login_user(username):
    try:
        # host, dbname, user, password = connection_constants()
        # connect_str = "dbname='{}' user='{}' host='{}' password='{}'".format(dbname, user, host, password)
	# connection = psycopg2.connect(connect_str)
	
	urllib.parse.uses_netloc.append('postgres')
	url = urllib.parse.urlparse(os.environ.get('DATABASE_URL'))
	connection = psycopg2.connect(
    		database=url.path[1:],
    		user=url.username,
    		password=url.password,
    		host=url.hostname,
    		port=url.port
	)

        cursor = connection.cursor()
        connection.autocommit = True
        cursor = connection.cursor()
        query = "SELECT password FROM users WHERE username=%s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        if result is not None:
            result = result[0]
    except psycopg2.DatabaseError as exception:
        print(exception)
        result = None
    finally:
        if connection:
            connection.close()
    return result

if __name__ == '__main__':
    pass
