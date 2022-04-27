
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_wtf.csrf import CSRFProtect 
# modelos
#from models.ModelUser import ModelUser
from models.ModelUser import ModelUser
# entidades
from models.entities.User import User
#https://www.geeksforgeeks.org/login-and-registration-project-using-flask-and-mysql/
app = Flask(__name__)
csrf = CSRFProtect()

app.secret_key = 'clavebelica1'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'veteribelica'

mysql = MySQL(app) # db 
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(mysql,id)

@app.route('/')
def index():
    return redirect(url_for('login'))

def status_404():
    return render_template('no_existe.html'),404

#https://open.spotify.com/playlist/4CtnDUfXLdiMxlYTReoTbV?si=e5aa7d6f47884df5
@app.route('/redireccionar/<tipo>/<id>', methods=['GET', 'POST'])
def redireccionar(tipo, id):
    print(type(tipo))
    #logged_user.tipoUser
    cliente = 'C'
    staff = 'S'
    ventas = 'V'
    if tipo == cliente:
        return redirect(url_for('menu_cliente', id = id))
    if tipo == staff:
        return redirect(url_for('inicioStaff'))
    if tipo == ventas:
        return redirect(url_for('ventas'))

@app.route('/login', methods =['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form['user'])
        print(request.form['pass'])
        user = User(0,request.form['user'], request.form['pass'])
        logged_user = ModelUser.login(mysql,user)
        if logged_user!= None:
            print("usuario logueado difernte a no")
            if logged_user.password:
                login_user(logged_user)
                print("usuario logeado...")
                #print(login_user)
                typeUser = ModelUser.get_type_by_user(mysql,request.form['user'])
                print(typeUser)
                uid = ModelUser.get_id_by_user(mysql,request.form['user'])

                #session['tipoUser'] = typeUser
                #user_type = ModelUser.get_by_id(mysql,user)
                #print(user_type)
                return redirect(url_for('redireccionar', tipo = typeUser, id = uid))
            else:

                flash("invalid password")
        else:
            flash("User not found ...")
            return redirect(url_for('login'))
    if request.method == 'GET':
        return render_template('login.html')
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/menu_cliente/<id>', methods =['GET', 'POST'])
def menu_cliente(id):
    if request.method == 'GET':
        #iduser = "1"
        iduser = id
        cur = mysql.connection.cursor()
        cur.execute('SELECT idmascota, nombreMascota, raza FROM mascotas WHERE idusuario = ' + iduser)
        datosMascotas = cur.fetchall()
        print(datosMascotas)
        cur1 = mysql.connection.cursor()
        cur1.execute('SELECT M.nombreMascota, C.fechaCita FROM citas C JOIN mascotas M ON M.idmascota = C.idanimal JOIN usuarios U ON M.idusuario = U.idusuario WHERE U.idusuario = ' + iduser)
        #SELECT M.nombreMascota FROM citas C JOIN mascotas M ON M.idmascota = C.idanimal JOIN usuarios U ON M.idusuario = U.idusuario WHERE U.idusuario = '1';
        datosCitas = cur1.fetchall()
        cur2 = mysql.connection.cursor()
        cur2.execute('SELECT M.nombreMascota, R.fechareceta, R.prescripcion FROM recetas R JOIN mascotas M ON R.idanimal = M.idmascota JOIN usuarios U ON U.idusuario = M.idusuario WHERE U.idusuario = ' + iduser)
        datosRecetas = cur2.fetchall()
        return render_template('menu_cliente.html',idc = iduser, mascotas = datosMascotas, citas = datosCitas, recetas = datosRecetas)

@app.route('/agregar_mascota/<id>', methods =['GET', 'POST'])
def agregar_mascota(id):
    if request.method == 'GET':
        #usrid = cookie
        return render_template('agregar_mascota.html', id = id )
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

@app.route('/agregar_mascota', methods=['POST'])
def agregar_mascota_post():
    if request.method == 'POST':
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
        return redirect(url_for('login'))

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

@app.route('/agregar_receta/<id>', methods =['GET', 'POST'])
def agregar_receta(id):
    if request.method == 'GET':
        return render_template('agregar_receta.html', id = id)

@app.route('/agregar_receta', methods =['POST'])
def agregar_receta_post():
    a = request.form['id']
    b = request.form['receta']
    cursor = mysql.connection.cursor()
    cursor. execute('INSERT INTO recetas (idanimal, prescripcion) VALUES(%s, %s)', (a,b,))
    mysql.connection.commit()
    return redirect(url_for('inicioStaff'))


@app.route('/guardar_cita', methods = ['POST'])
def guardar_cita():
    if request.method == 'POST':
        a = request.form['idmascota']
        b = request.form['fecha']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO citas (fechaCita, idanimal) VALUES(%s, %s)', (b, a,))
        mysql.connection.commit()
        print("exito en subir la cita")
        return redirect(url_for('menu_cliente'))

@app.route('/menu_staff', methods=['GET', 'POST'])
def inicioStaff():
    if request.method == 'GET':
        return render_template('menu_staff.html')

@app.route('/agregar_usuarios', methods =['POST', 'GET'])
def agregar_usuarios():
    if request.method == 'POST':
        a = request.form['user']
        b = request.form['pass']
        c = request.form['tipo']
        cursor = mysql.connection.cursor()
        cursor. execute('INSERT INTO usuarios (user, password, tipoUser) VALUES(%s, %s, %s)', (a,b,c,))
        mysql.connection.commit()
        return redirect(url_for('inicioStaff'))
    elif request.method == 'GET':
        return render_template('menu_usuarios.html')

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

@app.route('/ventas', methods=['GET', 'POST'])
def ventas():
    if request.method == 'POST':
        a = request.form['insumo']
        b = request.form['cantidad']
        c = request.form['precio']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO ventas (insumo, cantidad, precio) VALUES(%s,%s,%s)',(a,b,c,))
        mysql.connection.commit()
        return redirect(url_for('ventas'))
    if request.method == 'GET':
        return render_template('ventas.html')

@app.route('/ventas_totales', methods=['GET'])
def ventas_totales():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('SELECT idventa, insumo, cantidad, precio, fecha from ventas')
        data = cur.fetchall()
        print(data)
        return render_template('ventas_totales.html', ventas=data)

if __name__ == '__main__':
    app.run(debug=True, port=2000)
    app.error_handler(404,status_404)