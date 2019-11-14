import os
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
dir_path = Path(os.path.dirname(os.path.realpath(__file__)))
path = dir_path / '..'

# Database initialisation
FILE_PATH = f'{path}/db.sqlite3'
DB_URI = 'sqlite+pysqlite:///{file_path}'
db_config = {
    'SQLALCHEMY_DATABASE_URI': DB_URI.format(file_path=FILE_PATH),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
}
db = SQLAlchemy()
