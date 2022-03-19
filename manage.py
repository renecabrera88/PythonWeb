from app import create_app

from flask_script import Manager

"""aqui importamos el diccionario con la configuracion
ya que ahi estan las clases"""
from config import config

config_class = config['development']

"""aqui le pasamos los parametros obtenidos del 
diccionario que la configuracionfue extraido y pasado a 
config_class, asi cada vez que se guarde y como esta modo debug true se
reiniciara automaticamente"""
app = create_app(config_class)

if __name__ == '__main__':

    manager = Manager(app)
    manager.run()


"""Para ejecutar:  python manage.py runserver"""