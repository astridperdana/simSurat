from flask import Flask, render_template, request, redirect
from models import User

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
        ambil_data = model.getDataUser()
        print(ambil_data)
        if model.auth():
            return render_template('login_sukses.html', username = model.username)
        else:
            return render_template('login_gagal.html')
    else:
        return render_template('login_form.html')


if __name__ == '__main__':
    app.run(debug=True)