from flask import Flask

# -- Init --
app = Flask(__name__)
app.config.from_object(__name__)

#                                                             Password       Container           Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:tercer_parcial@tercer_parcial:3306/proyecto_bd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False