from flask import Flask
"""gracias a esta libreria se puede integrar bootstrap al proyecto"""
from flask_bootstrap import Bootstrap

from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

"""instanciamos bootstrap"""
bootstrap = Bootstrap()
"""crao una intancias"""
csrf = CSRFProtect()
"""importo page para decirl al 
servidor cuales son las rutas"""
from .views import page



"""la funcion create_app recibira como parametro una clase de 
configuracion. No olvidar que esta funcion esta siendo llamada 
dentro del archivo manage.py, donde se manda este parametro con
el nombre config_class y aqui se recibe como config"""
def create_app(config):
    """nuestro servidor se configurara a partir de la clase config
    el cual sera tratado como un objeto en la siguiente linea y la implermentacion
    lo hare mediente herencia de template"""
    app.config.from_object(config)

    """asocio mi instancia de csrf con la aplicacion, ose con el servidor. 
    y en el archivo config creamo nuestra clave secreta """
    csrf.init_app(app)

    """asignamos app a bottstrap"""
    bootstrap.init_app(app)

    """aqui le damos las rutas a app"""
    app.register_blueprint(page)
    return app


"""Al ejecutar da un error de :
ModuleNotFoundError: No module named 'flask._compat'
Para solucionar el error ve a la ruta donde te marca el error en la carpeta flask-script
 y en el archivo init.py cambia la linea 15 de from flask._compat import text_type
  a from flask_script._compat import text_type
"""

