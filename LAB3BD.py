from benches import *
from config import *



run = {
    'sqlite': sqlite,
    'pandas': pandas,
    'psycopg2': psycopg2,
    'duckdb': duckdb,
    'sqlalchemy': sqlalchemy,
    }

run[LIB]()
