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

Проверка была осуществлена на 2-ух наборах данных.
# tiny
![image](https://github.com/AlexVenem/Lab3FinR/assets/130144087/2bda8c0b-1698-4490-aadf-003b98244360)
![image](https://github.com/AlexVenem/Lab3FinR/assets/130144087/7e3806d7-2521-4e24-83c7-ae9af73cc1ff)
# Big
![image](https://github.com/AlexVenem/Lab3FinR/assets/130144087/0d99f8f7-7b20-4ce4-9d7b-96e8c378f517)
![image](https://github.com/AlexVenem/Lab3FinR/assets/130144087/1075e7c3-3a53-4d8b-b14c-7a82ae6ea9c3)
# Мнение о библиотеках
Изучение этой темы встретило меня не очень дружелюбно. Однако по итогу я могу сказать, что результат оказался познавательным. DuckDB показала себя, как самая быстрая система (быстрее SQLite3, как и утверждают источники рекламирующие DuckDB). Psycopg2, Pandas показали себя лучше на большом наборе данных. Итоги SQLite и SQLAlchemy схожи из-за того, что последнее базируется на своём собрате.
Каждая библиотека имеет свои плюсы и минусы, что в сумме даёт весьма хорошую базу для работы с наукой о данных. Python является, по моему мнению, лучшим из общеизвестных языков для работы с большими базами данных.




А ещё изначально csv файлы были немного поломаны, колонка airport_fee была разделена на две колонки.




# Примеры работы программы
SQLite
![image](https://github.com/AlexVenem/Lab3FinR/assets/130144087/6ce04fa6-4d8a-48ad-bfd7-62d2bf5b4636)
Pandas
![image](https://github.com/AlexVenem/Lab3FinR/assets/130144087/d2a8ce0f-66c8-4ef2-9379-27cd8b5e7d01)
![image](https://github.com/AlexVenem/Lab3FinR/assets/130144087/d96c5179-55d1-41fc-a52a-d49fae419a3c)
