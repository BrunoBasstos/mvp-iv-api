# models/__init__.py
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importando os elementos definidos no modelo
from models.base import Base
from models.titanic import Titanic
from models.passenger import Passenger


db_path = "database/"
# se o diretorio não existir, então cria
if not os.path.exists(db_path):
    os.makedirs(db_path)

# define o caminho do banco
db_url = 'sqlite:///%s/titanic.sqlite3' % db_path

# cria o engine do banco
engine = create_engine(db_url, echo=False)

# cria a sessão do banco
Session = sessionmaker(bind=engine)

# cria o banco se não existir
if not database_exists(engine.url):
    create_database(engine.url)

# cria as tabelas, caso não existam
Base.metadata.create_all(engine)
