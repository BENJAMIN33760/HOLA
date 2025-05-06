from flask import Flask, render_template, request
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

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/task/create')
def create_task():
    return render_template('create_task.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contraseña = request.form['contrasena']
        return f"<p>{nombre}, {correo}, {contraseña}<p>"
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)