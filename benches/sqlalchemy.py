from sqlalchemy import create_engine, text
from time import perf_counter 
from config import *


def start():
    url_to_db = f'postgresql://{DB_PARAMS["user"]}:{DB_PARAMS["password"]}@{DB_PARAMS["host"]}:{DB_PARAMS["port"]}/{DB_PARAMS["dbname"]}'
    engine = create_engine(url_to_db)
    cursor = engine.connect()
    
    One = """SELECT "VendorID", COUNT(*)
        FROM trips GROUP BY 1;"""
    Two = """SELECT "passenger_count", AVG("total_amount")
           FROM trips GROUP BY 1;"""
    Three = """SELECT "passenger_count", DATE_PART('Year', tpep_pickup_datetime::date), COUNT(*)
           FROM trips GROUP BY 1, 2;"""
    Four = """SELECT "passenger_count", DATE_PART('Year', tpep_pickup_datetime::date), ROUND("trip_distance"), COUNT(*)
           FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;"""

    res_time = 0
    for i in range(EX_COUNT):
        Stime = perf_counter()
        cursor.execute(text(One))
        Ftime = perf_counter()
        res_time = Ftime - Stime
    res_time /= EX_COUNT
    print(f"Query 1: {round(res_time, 2)} sec")
    res_time = 0
    for i in range(EX_COUNT):
        Stime = perf_counter()
        cursor.execute(text(Two))
        Ftime = perf_counter()
        res_time = Ftime - Stime
    res_time /= EX_COUNT
    print(f"Query 2: {round(res_time, 2)} sec")
    res_time = 0
    for i in range(EX_COUNT):
        Stime = perf_counter()
        cursor.execute(text(Three))
        Ftime = perf_counter()
        res_time = Ftime - Stime
    res_time /= EX_COUNT
    print(f"Query 3: {round(res_time, 2)} sec")
    res_time = 0
    for i in range(EX_COUNT):
        Stime = perf_counter()
        cursor.execute(text(Four))
        Ftime = perf_counter()
        res_time = Ftime - Stime
    res_time /= EX_COUNT
    print(f"Query 4: {round(res_time, 2)} sec")
    
    cursor.close()
    engine.dispose()