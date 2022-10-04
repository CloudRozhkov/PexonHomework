import math
import time
import sqlite3

class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()


    def addZert(self, name, zertifikat, date):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO userszet VALUES (NULL, ?, ?, ?, ?)", (name, zertifikat, date, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print ("Fehler beim Hinzufügen von Zertifikaten " +str(e))
            return False
        return True

    def getZert(self):
        sql = """SELECT * FROM userszet"""
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Fehler beim DB")
        return []