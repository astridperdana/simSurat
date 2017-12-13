import sqlite3, os

DB = os.getcwd() + '/database.db'

class User(object):
    def __init__(self, username = '', password = '', flag = 0):
        self.username = username
        self.password = password
        self.flag = flag

    def setUsername(self, username):
        self.username = username
    
    def setPassword(self, password):
        self.password = password

    def setFlag(self, flag):
        self.flag = flag

    def tambah(self):
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users VALUES(?,?,?)", (self.username, self.password, self.flag))
        conn.commit()
        cursor.close()
        conn.close()

    def ubah(self):
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE users SET password = ?, flag = ?
        WHERE username = ?
        ''', (self.password, self.flag, self.username))
        conn.commit()
        cursor.close()
        conn.close()

    def hapus(self):
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE username=?", (self.username))
        conn.commit()
        cursor.close()
        conn.close()

    def load(self, id):
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        for username, password, flag in cursor.execute("SELECT * FROM users"):
            if username == id:
                self.username = username
                self.password = password
                self.flag = flag
                break
        cursor.close()
        conn.close()

    def getDataUser(self):
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        for username, password, flag in cursor.execute("SELECT * FROM users"):
            if username == self.username:
                return [username, password, flag]
        cursor.close()
        conn.close()

    def auth(self):
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        for username, password in cursor.execute("SELECT * FROM users"):
            if self.username == username and self.password == password:
                return True
        else:
            return False
        cursor.close()
        conn.close()
