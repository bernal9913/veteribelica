
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
  
#https://www.geeksforgeeks.org/login-and-registration-project-using-flask-and-mysql/
app = Flask(__name__)
  
  
app.secret_key = 'your secret key'
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'veteribelica'
  
mysql = MySQL(app)
  
@app.route('/')
def login():
    return 'serse'

@app.route('/menu_cliente', methods =['GET', 'POST'])
def cliente():
    if request.method == 'GET':
        iduser = "1"
        cur = mysql.connection.cursor()
        cur.execute('SELECT idmascota, nombreMascota, raza FROM mascotas WHERE idusuario = ' + iduser)
        datosMascotas = cur.fetchall()
        print(datosMascotas)
        cur1 = mysql.connection.cursor()
        cur1.execute('SELECT M.nombreMascota FROM citas C JOIN mascotas M ON M.idmascota = C.idanimal JOIN usuarios U ON M.idusuario = U.idusuario WHERE U.idusuario = ' + iduser)
        #SELECT M.nombreMascota FROM citas C JOIN mascotas M ON M.idmascota = C.idanimal JOIN usuarios U ON M.idusuario = U.idusuario WHERE U.idusuario = '1';
        return render_template('menu_cliente.html', mascotas = datosMascotas)

@app.route('/agregar_mascota', methods =['GET', 'POST'])
def agregar_mascota():
    if request.method == 'GET':
        #usrid = cookie
        return render_template('agregar_mascota.html')
    elif request.method == 'POST':
        a = request.form['iduser']
        b = request.form['nombreMascota']
        c = request.form['raza']
        print(b)
        cursor = mysql.connection.cursor()
        d = b.capitalize()
        e = c.capitalize()
        cursor.execute('INSERT INTO mascotas (idusuario, nombreMascota, raza) VALUES(%s,%s,%s)',
        (a,d,e,))
        mysql.connection.commit()
        print("animal subido con exito")
        return render_template('menu_cliente.html')

@app.route('/eliminar_mascota', methods=['POST', 'GET'])
def eliminar_mascota():
    if request.method == 'GET':
        #httpsiduser = cookie
        
        return render_template('eliminar_mascota.html')
    elif request.method == 'POST':
        #query belica para eliminar a la mascota
        print('eliminar')

@app.route('/agendar_cita/<string:idmascota>', methods=['POST', 'GET'])
def agendar_cita(idmascota):
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM mascotas WHERE idmascota = ' + idmascota)
        data = cur.fetchall()
        print(data)
        return render_template('agendar_cita.html', masc = data)

@app.route('/guardar_cita', methods = ['POST'])
def guardar_cita():
    if request.method == 'POST':
        a = request.form['idmascota']
        b = request.form['fecha']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO citas (fechaCita, idanimal) VALUES(%s, %s)', (b, a,))
        mysql.connection.commit()
        print("exito en subir la cita")
        return redirect(url_for('/menu_cliente'))

@app.route('/menu_staff', methods=['GET', 'POST'])
def inicioStaff():
    if request.method == 'GET':
        return render_template('menu_staff.html')

@app.route('/usuarios', methods=['POST'])
def busc_usuarios():
    if request.method == 'POST':
        a = request.form.get('user')
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios WHERE user = "' + a + '"')
        data = cur.fetchall()
        return render_template('usuarios.html', usr = data)


@app.route('/usuario/<string:iduser>', methods=['POST', 'GET'])
def usr_mascota(iduser):
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM mascotas WHERE idusuario = ' + iduser)
        data = cur.fetchall()
        print(data)
        return render_template('usuario_mascotas.html', masc = data)

@app.route('/agregar_cita_staff1', methods=['GET', 'POST'])
def citaStaff1():
    if request.method == 'GET':
        return render_template('cita_staff1.html')

@app.route('/cita_staff2', methods =['POST'])
def citaStaff2():
    if request.method == 'POST':
        a = request.form['nombre']
        cur = mysql.connection.cursor()
        cur.execute('SELECT idusuario, user FROM usuarios WHERE user = ' + a)
        data = cur.fetchall()
        return render_template('cita_staff2.html', datos=data)

if __name__ == '__main__':
    app.run(debug=True, port=2000)