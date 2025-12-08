from flask import Flask
from flask_cors import CORS
from config import Config
from database import db

from routes.user_routes import user_bp
from routes.room_routes import room_bp
from routes.item_routes import item_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)

    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(room_bp, url_prefix="/api/rooms")
    app.register_blueprint(item_bp, url_prefix="/api/items")

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
