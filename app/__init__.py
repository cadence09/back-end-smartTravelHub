from flask import Flask;
from flask_sqlalchemy import SQLAlchemy;
from flask_migrate import Migrate;
import os;
from dotenv import load_dotenv
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)
    print("db,",db)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")

    db.init_app(app)
    migrate.init_app(app,db)

    CORS(app)
    from .routes import travel_posts_bp;
    app.register_blueprint(travel_posts_bp)
    from app.models.travel_posts import Travelposts;
    
    return app