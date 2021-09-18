# -------------------------------------------------------------------------
#  Database handler
# -------------------------------------------------------------------------
# import MySQLdb and os libraries to interact with the mysql db
import MySQLdb
import os


class DbHandler:
    # declaring the constructor for DbHandler Class
    def __init__(self):
        self.m_host = '173.194.110.126'  # server IP
        self.m_user = 'db_team02'  # username
        self.m_password = 'kxosktvi' # password
        self.m_default_db = 'db_team02'  # database name
        self.m_unixSocket = '/cloudsql/dbcourse2015:mysql'  # Google APP engine socket
        self.m_charset = 'utf8'  # encoding
        self.m_port = 3306  # port to connect to
        self.m_DbConnection = None  # attribute to store the connection

    def connectDb(self):
        if self.m_DbConnection is None:  # if connection hasn't been established
            env = os.getenv('SERVER_SOFTWARE')
            if env and env.startswith('Google App Engine/'):  # if working on google ap engine, connect using socket
                self.m_DbConnection = MySQLdb.connect(unix_socket=self.m_unixSocket,
                                                      user=self.m_user, passwd=self.m_password,
                                                      charset=self.m_charset, db=self.m_default_db)
            else:  # if working locally, connect using specific server IP address
                self.m_DbConnection = MySQLdb.connect(host=self.m_host, user=self.m_user,
                                                      passwd=self.m_password,db=self.m_default_db)

    def disconnectDb(self):  # method to disconnect from server
        if self.m_DbConnection:  # if connection has bee established
            self.m_DbConnection.close()

    def commit(self):  # method to save data to database
        if self.m_DbConnection:  # if connection has been established
            self.m_DbConnection.commit()

    def get_cursor(self):  # method to get cursor to execute actions
        if self.m_DbConnection:  # if connection has bee established
            return self.m_DbConnection.cursor()

    # method takes value column name and table name as arguments, returns True if value exists in DB
    def exists(self,value,column,table_name):
        cursor = self.get_cursor()
        query = "SELECT * FROM {} WHERE {} = \"{}\"".format(table_name,column,value)
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        return len(data) > 0



