from flask import *
from flask_cors import CORS
from sql import *
import json
app, appconfig, attitudes = Flask(__name__), {"host": "192.168.43.19", "port": 5000, "secret-key": "we9y38KDm"}, {"do-login": "", "do-register": ""}
app.secret_key = appconfig["secret-key"]
CORS(app)

@app.route('/', methods=["GET", "POST"])
def index():
    if not 'usuario' in session:
        return forms()
    return home()

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return redirect(url_for('index'))
    if request.method == "POST":
        if not request.get_json(): return 'No se recibieron las credenciales de acceso'
        Package = request.get_json()
        if not Package.get('user'): return 'No se recibió el usuario'
        if not Package.get('password'): return 'No se recibió la contraseña'
        User, Password = Package.get('user'), Package.get('password')
        DoLogin(User, Password)
        return redirect(url_for('index'))

@app.route('/create', methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return redirect(url_for('index'))
    if request.method == "POST":
        if not request.get_json(): return 'No se recibieron las credenciales de acceso'
        Package = request.get_json()

        if not Package.get('name'): return 'No se recibió el nombre'
        if not Package.get('user'): return 'No se recibió el usuario'
        if not Package.get('password'): return 'No se recibió la contraseña'
        if not Package.get('pfp'): 
            Pic = 'https://icon-icons.com/icons2/3868/PNG/512/profile_circle_icon_242774.png'
        else:
            Pic = Package.get('pfp')
        User, Password, Name = Package.get('user'), Package.get('password'), Package.get('name')
        DoCreate(Name, User, Password, Pic)
        return redirect(url_for('index'))

def forms():
    return render_template('forms.html')
def home():
    return render_template('panel.html')
def DoLogin(user, password):
    #hacer un login
def DoCreate(name, user, passowrd, pic):
    #hacer un registro
@app.errorhandler(404)
#no existe el recurso solicitado
def e404(error):
    return render_template('e404.html')



@app.errorhandler(401)
#no se tiene permitido acceder al recurso
def e401(error):
    return render_template('e401.html')


if __name__ == '__main__':
    app.run(debug=True, host=appconfig["host"], port=appconfig["port"])