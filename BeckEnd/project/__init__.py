from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from project.ORM.route import __init_routes

db = SQLAlchemy()
binary_tree = None

def create_app() -> Flask:
    app = Flask(__name__)
    __init_binary_tree()
    __init_db(app)
    __init_routes(app)

    print("Creating App is End")

    return app

def __init_binary_tree():
    global binary_tree
    from project.BinaryTree import BinaryTree
    binary_tree = BinaryTree()


def __init_db(app: Flask) -> None:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:RTXSQl__23!sQl@127.0.0.1:3306/BinaryTree'

    if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
        create_database(app.config['SQLALCHEMY_DATABASE_URI'])
        print("Create NEW database")

    db.init_app(app)

    import project.ORM.domain
    with app.app_context():
        db.create_all()
        print("Create tables (if not exists)")

