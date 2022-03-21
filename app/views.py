"""esta es la clase blueprint de flask para trabajar rutas"""
from flask import Blueprint
"""render template es una funcion que permite renderizar los .htmls"""
from flask import render_template, request

from .forms import LoginForm

"""instancia de blueprint puedo definir las rutas"""
page = Blueprint('page', __name__)

"""no olvidar que los errores en python deben devolverse
en este caso, devolveremos error 404 de direccion url not encontrada.
recivimos el error en app_errorhandler, lo pasamos a la funcion 
y finalmente lo devolvemnos para que el front haga algo con ese error. siempre hay 
que devolver los errores, ya que de no devolverlo el cliente recibirá un 200"""
@page.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

@page.route('/')
def index():
    """con render template automaticamente va a buscar el nmbre del html a templates"""
    return render_template('index.html')

"""Esta ruta renderiza template con ingleso de usuario y la data dedebera
ser validada por el wtforms."""
@page.route('/login', methods=['GET', 'POST'])
def login():
    """instanciamos LoginForm y pasamos los request a la instancia"""
    form = LoginForm(request.form)
    """preguntamos si le metodo es POST y valido los datos"""
    if request.method == 'POST' and form.validate():
        """Si es post, ya podemos crear la session"""
        print(form.username.data)
        print(form.password.data)
        print('Nueva sesion creada')

    """form lo enviamos como parametro"""
    return render_template('auth/login.html', title='Login', form=form)

