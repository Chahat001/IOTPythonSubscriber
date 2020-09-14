from __future__ import print_function
import mysql.connector
from mysql.connector import (connection, errorcode)
from datetime import date, datetime, timedelta
import os

class DataBase:

    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user = os.getenv("DATABASE_USER"), password=os.getenv("DATABASE_PASS"),
                                          host=os.getenv("DATABASE_ADDR"),
                                          database=os.getenv("DATABASE_NAME"))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)


    def writeData(self, s:str):
        cursor = self.cnx.cursor()

        time_now = datetime.now()
        add_Value_Query = ("INSERT INTO ${os.getenv(\"DATABASE_TABLE\")} "
               "(time, lux) "
               "VALUES (%s, %s)")
        #print("writing to datbase %s"%(s))
        cursor.execute(add_Value_Query, (time_now, s))

        self.cnx.commit()

        cursor.close()
        self.cnx.close()


    def clearTable(self):
        cursor = self.cnx.cursor()
        query = ("TRUNCATE TABLE ${os.getenv(\"DATABASE_TABLE\")}")

        cursor.execute(query)

        self.cnx.commit()

        cursor.close()
        self.cnx.close()


    def getData(self):
        cursor = self.cnx.cursor()

        query = ("SELECT time, lux FROM ${os.getenv(\"DATABASE_TABLE\")}")

        cursor.execute(query)
        beginTime = 0
        list_lux = []
        list_time = []
        for (time, lux) in cursor:
            if beginTime == 0:
                beginTime = time.total_seconds()
            list_lux.append(int(lux))
            list_time.append(int(time.total_seconds()-beginTime))

        cursor.close()
        self.cnx.close()

        return (list_lux, list_time)













