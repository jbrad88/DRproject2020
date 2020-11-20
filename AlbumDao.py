import mysql.connector

class AlbumDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'music'
        )
        #print ("connection made")

    def create(self, album):
        cursor = self.db.cursor()
        sql = "insert into albums (code, artist, title, price) values (%s,%s,%s,%s)"
        values = [
            album['code'],
            album['artist'],
            album['title'],
            album['price']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from albums'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findById(self, code):
        cursor = self.db.cursor()
        sql = 'select * from albums where code = %s'
        values = [ code ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)


    def update(self, album):
        cursor = self.db.cursor()
        sql = "update albums set title = %s, artist = %s, price = %s where code = %s"
        values = [
            album['title'],
            album['artist'],
            album['price'],
            album['code']

        ]
        cursor.execute(sql, values)
        self.db.commit()
        return album
    
    def delete(self, code):
        cursor = self.db.cursor()
        sql = 'delete from albums where code = %s'
        values = [ code ]
        cursor.execute(sql, values)

        return {}



    def convertToDict(self, result):
        colnames = ['code','artist','title','price']
        album = {}

        if result: 
            for i , colName in enumerate(colnames):
                value = result[i]
                album[colName] = value
        return album

albumDao = AlbumDao()