"""aqui van los configuraciones globales"""
class Config:
    SECRET_KEY = 'miclavesecreta'


"""aqui van las configuraciones
 especificas para el entorno de desarrollo"""
class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

"""archivo de configuracion de los diferentes entornos. Este archivo es muy importante
ya que aqui se configura los correos, bases de datos, etc"""