from wsgiref.validate import validator
from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField

"""en este formulario se colocan los conpos dentro de una clase, despues se mandan 
instancias en views para enviarlos como parametros al respectivo template clase
y poder renderizar los controles en el formulario, eso es gracias a wtforms, a esto se le 
llama pintar los formularios"""

class LoginForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50, message="El usuario esta fuera de rango")
    ])
    password = PasswordField('Password', [
        validators.data_required()  
    ])

