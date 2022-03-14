#!/usr/bin/env python3
import pymysql
import sys
import time

host='localhost'
user='root'
password = 'password'

try:
    # connect to the database with your credentials
    con = pymysql.connect(host=host, user=user, password=password, autocommit=True, local_infile=1)
    print(f'Connected to DB: {host}')
    cursor = con.cursor()
    cursor.execute("DROP DATABASE IF EXISTS StatifyDB;")
    cursor.execute("CREATE DATABASE StatifyDB;")
    print("Created DATABASE. Name: StatifyDB")

    cursor.execute("USE StatifyDB;")

    cursor.execute("""CREATE TABLE `countries` (`country_code` varchar(3) NOT NULL,
                                                `country_name` varchar(50) NOT NULL,
                                                PRIMARY KEY (`country_code`))
                                                ENGINE=InnoDB DEFAULT CHARSET=utf8mb4  COLLATE=utf8mb4_0900_ai_ci;""")
    print("Created countries table.")

    cursor.execute("""CREATE TABLE `indicators` (`indicator_code` varchar(50) NOT NULL,
                                                `indicator_name` varchar(200) NOT NULL,
                                                PRIMARY KEY (`indicator_code`))
                                                ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;""")
    print("Created indicators table.")

    cursor.execute("""CREATE TABLE `years` (`year` int NOT NULL,
                                            `five_yr_period` varchar(100) NOT NULL,
                                            `ten_yr_period` varchar(100) NOT NULL,
                                            `twenty_yr_period` varchar(100) NOT NULL,
                                            PRIMARY KEY (`year`))
                                            ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;""")
    print("Created years table.")

    cursor.execute("""CREATE TABLE `measurements` ( `country_code` varchar(3) NOT NULL,
                                                    `indicator_code` varchar(50) NOT NULL,
                                                    `year` int NOT NULL,
                                                    `measurement` DOUBLE,
                                                    PRIMARY KEY (`country_code`,`indicator_code`,`year`),
                                                    KEY `indicator_code` (`indicator_code`),
                                                    KEY `year` (`year`),
                                                    CONSTRAINT `measurements_ibfk_1` FOREIGN KEY (`country_code`) REFERENCES `countries` (`country_code`),
                                                    CONSTRAINT `measurements_ibfk_2` FOREIGN KEY (`indicator_code`) REFERENCES `indicators` (`indicator_code`),
                                                    CONSTRAINT `measurements_ibfk_3` FOREIGN KEY (`year`) REFERENCES `years` (`year`))
                                                    ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;""")
    print("Created measurements table.")
    print("Loading csv files...")
    cursor.execute("""LOAD DATA LOCAL INFILE '/home/alexandros/Desktop/Statify-data-visualizer/Data_config/Exported_data/csv/countries.csv'
                      INTO TABLE countries
                      FIELDS TERMINATED BY ',' ENCLOSED BY '"';""")
    print("Loaded countries csv to countries table.")
    cursor.execute("""LOAD DATA LOCAL INFILE '/home/alexandros/Desktop/Statify-data-visualizer/Data_config/Exported_data/csv/indicators.csv'
                      INTO TABLE indicators
                      FIELDS TERMINATED BY ',' ENCLOSED BY '"';""")
    print("Loaded indicators.csv to indicators table.")
    cursor.execute("""LOAD DATA LOCAL INFILE '/home/alexandros/Desktop/Statify-data-visualizer/Data_config/Exported_data/csv/years.csv'
                      INTO TABLE years
                      FIELDS TERMINATED BY ',' ENCLOSED BY '"';""")
    print("Loaded years.csv to years table.")
    cursor.execute("""LOAD DATA LOCAL INFILE '/home/alexandros/Desktop/Statify-data-visualizer/Data_config/Exported_data/csv/measurements.csv'
                      INTO TABLE measurements
                      FIELDS TERMINATED BY ',' ENCLOSED BY '"';""")
    print("Loaded measurements.csv to measurements table.")
    con.close()
except Exception as e:
    print(f'MySQL Error: {str(e)}')
    sys.exit(1)

