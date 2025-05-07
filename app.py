from flask import Flask, render_template, request, url_for, redirect, session
from config import Config
from models import db, Usuario, Tarea

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/tasks')
def list_tasks():
    tareas = ["Lavar la ropa", "Limpiar la casa", "Hacer la compra", "Estudiar para el examen", "Hacer ejercicio", "Leer un libro"]
    return render_template('tasks.html', tareas=tareas)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']

        usuario = Usuario.query.filter_by(correo=correo).first()
        if usuario and usuario.verificar_contrasena(contrasena):
            session["usuario_id"] = usuario.id 
            session["usuario_nombre"] = usuario.nombre
            return redirect(url_for('list_task'))
        else:
            return "Correo o contrasena incorrectos"
    return render_template('login.html')

@app.route('/task/create')
def create_task():
    return render_template('create_task.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        if Usuario.query.filter_by(correo=correo).first():
            return "El correo ya esta registrado"
        else:
            nuevo_usuario = Usuario(nombre=nombre, correo=correo)
            nuevo_usuario.colocar_contrasena(contrasena)
            db.session.add(nuevo_usuario)
            db.session.commit()
            return redirect(url_for('login'))
        return f"<p>{nombre}, {correo}, {contrasena}<p>"
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)