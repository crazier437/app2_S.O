import psycopg2
from flask import g
'''
def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            user="dbuser",
            password="secreto",
            host="db",
            port="5432",
            database="db"
         )
    return g.db
    '''
def get_db():
    
    db_user = os.environ['DB_USERNAME']
    db_password = os.environ['DB_PASSWORD']
    db_name = os.environ['DB_NAME']
    db_connection_name = os.environ['CLOUD_SQL_CONNECTION_NAME']

    if 'db' not in g and db_connection_name:
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        g.db = psycopg2.connect(
            user=db_user,
            password=db_password,
            host=unix_socket,
            database=db_name
        )
    return g.db
