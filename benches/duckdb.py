from config import *
import pandas as pd
import duckdb
from time import perf_counter

#duckdb.install_extension("SQLite")


def start():
    connection = duckdb.connect('postgres.db')
    cursor = connection.cursor()
    

    One = """SELECT "VendorID", COUNT(*)
        FROM trips GROUP BY 1;"""
    Two = """SELECT "passenger_count", AVG("total_amount")
           FROM trips GROUP BY 1;"""
    Three = """SELECT "passenger_count", STRFTIME('%Y', "tpep_pickup_datetime"), COUNT(*)
           FROM trips GROUP BY 1, 2;"""
    Four = """SELECT "passenger_count", STRFTIME('%Y', "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*)
           FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;"""
    
    
    res_time = 0
    for i in range(EX_COUNT):
        Stime = perf_counter()
        cursor.execute(One)
        Ftime = perf_counter()
        res_time = Ftime - Stime
    res_time /= EX_COUNT
    print(f"Query 1: {round(res_time, 2)} sec")
    res_time = 0
    for i in range(EX_COUNT):
        Stime = perf_counter()
        cursor.execute(Two)
        Ftime = perf_counter()
        res_time = Ftime - Stime
    res_time /= EX_COUNT
    print(f"Query 2: {round(res_time, 2)} sec")
    res_time = 0
    for i in range(EX_COUNT):
        Stime = perf_counter()
        cursor.execute(Three)
        Ftime = perf_counter()
        res_time = Ftime - Stime
    res_time /= EX_COUNT
    print(f"Query 3: {round(res_time, 2)} sec")
    res_time = 0
    for i in range(EX_COUNT):
        Stime = perf_counter()
        cursor.execute(Four)
        Ftime = perf_counter()
        res_time = Ftime - Stime
    res_time /= EX_COUNT
    print(f"Query 4: {round(res_time, 2)} sec")    

    cursor.close
    connection.close

