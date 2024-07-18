import psycopg2
from psycopg2 import pool

Connection_pool = pool.SimpleConnectionPool(
    1, 20,
    database ="biblioteca3A",
    user="postgres",
    password="perro12345",
    host="localhost",
    port="5432"
)


def conectar():
    return Connection_pool.getconn()

def desconectar(conn):
    Connection_pool.putconn(conn)
