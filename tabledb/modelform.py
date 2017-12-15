import sqlite3, os

DB = os.getcwd() + '/database.db'

class Form1(object):
    def __init__(self, form1id = '', nrp = '', nama = '', ttl = '', email = '', alamat_asal = '', sks='', ipk = '', tanggal_proposal = '', dospem_ta = '', judul_ta = ''):
        self.form1id = form1id
        self.nrp = nrp
        self.nama = nama
        self.ttl = ttl
        self.email = email
        self.alamat_asal = alamat_asal
        self.sks = sks
        self.ipk = ipk
        self.tanggal_proposal = tanggal_proposal
        self.dospem_ta = dospem_ta
        self.judul_ta = judul_ta

    def setJudulTa(self, judul_ta):
        self.judul_ta = judul_ta

    def setDospemTa(self, dospem_ta):
        self.dospem_ta = dospem_ta

    def setIpk(self, ipk):
        self.ipk = ipk

    def setSks(self, sks):
        self.sks = sks

    def setAlamatAsal(self, alamat_asal):
        self.alamat_asal = alamat_asal

    def setEmail(self, email):
        self.email = email

    def setTtl(self, ttl):
        self.ttl = ttl

    def setNama(self, nama):
        self.nama = nama

    def setForm1Id(self, form1id):
        self.form1id = form1id

    def setNrp(self, nrp):
        self.nrp = nrp

    def tambah(self):
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO form1 VALUES(?,?,?,?,?,?,?,?,?,?,?)", (self.form1id, self.nrp, self.nama, self.ttl, self.email, self.alamat_asal, self.sks, self.ipk, self.tanggal_proposal, self.dospem_ta, self.judul_ta))
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
        for username, password, flag in cursor.execute("SELECT * FROM users"):
            if self.username == username and self.password == password:
                return True
        else:
            return False
        cursor.close()
        conn.close()
