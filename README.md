# LAB3BD

Задача: создание и испытание бенчмарков, реализованных на пяти библиотеках(SQLite3, DuckDB, Pandas, Psycopg2, SQLAlchemy).

Для выполнения задания были дополнительно использованы Docker Engine и PGAdmin.

Проект представляет собой 5 python файлов с бенчмарками, главный файл(LAB3BD), конфиг и инит файлы.

Для проверки библиотек были использованы 4 SQL запроса:
```sql
SELECT VendorID, count(*) FROM trips GROUP BY 1;
SELECT passenger_count, avg(total_amount) FROM trips GROUP BY 1;
SELECT passenger_count, extract(year from tpep_pickup_datetime), count(*) FROM trips GROUP BY 1, 2;
SELECT passenger_count, extract(year from tpep_pickup_datetime), round(trip_distance), count(*) FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;
```


































![image](https://github.com/AlexVenem/Lab3FinR/assets/130144087/6ce04fa6-4d8a-48ad-bfd7-62d2bf5b4636)
