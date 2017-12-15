from flask import Flask, render_template, request, redirect
from models import User
from modelform import Form1

app = Flask(__name__)

@app.route('/')
def index():
    import sqlite3, os
    databaseName = os.getcwd() + '/database.db'
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
    container = []
    for username, password, flag in cursor.execute('SELECT * FROM users'):
        model = User(username, password, flag)
        container.append(model)
    cursor.close()
    conn.close()
    return render_template('index.html', container = container)

@app.route('/tambahUser', methods = ['POST', 'GET'])
def tambah():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        flag = int(request.form['flag'])
        model = User(username, password, flag)
        model.tambah()
        return redirect('http://localhost:5000')
    else:
        return render_template('tambah_form.html')

@app.route('/ubahUser/<id>', methods = ['POST', 'GET'])
def ubah(id):
    model = User()
    model.load(id)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        flag = int(request.form['flag'])
        model.setUsername(username)
        model.setPassword(password)
        model.setFlag(flag)
        model.ubah()
        return redirect('http://localhost:5000')
    else:
        return render_template('ubah_form.html', model=model)

@app.route('/hapusUser/<id>')
def hapus(id):
    model = User()
    model.load(id)
    model.hapus()
    return redirect('http://localhost:5000')

@app.route('/loginUser', methods = ['POST', 'GET'])
def login():
    model = User()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        model.setUsername(username)
        model.setPassword(password)
        kembalian = model.getDataUser()
        if model.auth():
            if kembalian[2] == 1:
                return render_template('login_sukses_mhs.html', username = model.username)
            else:
                return render_template('login_sukses_tu.html', username = model.username)
        else:
            return render_template('login_gagal.html')
    else:
        return render_template('login_form.html')

@app.route('/tambahForm1', methods = ['POST', 'GET'])
def tambahForm1():
    if request.method == 'POST':
        form1id = request.form['form1_id']
        nrp = request.form['nrp']
        nama = request.form['nama']
        ttl = request.form['ttl']
        email = request.form['email']
        alamat_asal = request.form['alamat_asal']
        sks = request.form['sks']
        ipk = request.form['ipk']
        tanggal_proposal = request.form['tanggal_proposal']
        dospem_ta = request.form['dospem_ta']
        judul_ta = request.form['judul_ta']
        model = Form1(form1id, nrp, nama, ttl, email, alamat_asal, sks, ipk, tanggal_proposal, dospem_ta, judul_ta)
        model.tambah()
        return redirect('http://localhost:5000')
    else:
        return render_template('tambah_form1.html')

@app.route('/tambahForm2', methods = ['POST', 'GET'])
def tambahForm2():
    if request.method == 'POST':
        return redirect('http://localhost:5000')
    else:
        return render_template('tambah_form2.html')

@app.route('/tambahForm3', methods = ['POST', 'GET'])
def tambahForm3():
    if request.method == 'POST':
        return redirect('http://localhost:5000')
    else:
        return render_template('tambah_form3.html')

@app.route('/tambahForm4', methods = ['POST', 'GET'])
def tambahForm4():
    if request.method == 'POST':
        return redirect('http://localhost:5000')
    else:
        return render_template('tambah_form4.html')


if __name__ == '__main__':
    app.run(debug=True)