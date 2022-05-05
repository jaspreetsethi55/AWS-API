import pymysql

class db:
    def __init__(self,db_host,db_user,db_pass,db_name,db_charset):
        self.db_host = db_host
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_name = db_name
        self.db_charset = db_charset
        
    def connect(self):
        return pymysql.connect(host=self.db_host,
                             user=self.db_user,
                             password=self.db_pass,
                             database=self.db_name,
                             charset=self.db_charset,
                             cursorclass=pymysql.cursors.DictCursor)
    
