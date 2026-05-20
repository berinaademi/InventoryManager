from flask import Flask
from flask_cors import CORS
from database import db
from flask import jsonify
from flask import Flask, send_from_directory


def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app)

    # Konfiguration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Blueprints innerhalb der Funktion importieren, um zirkuläre Importe zu vermeiden
    from routes.user_routes import user_bp
    from routes.room_routes import room_bp
    from routes.item_routes import item_bp

    # Blueprints registrieren
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(room_bp, url_prefix="/api/rooms")
    app.register_blueprint(item_bp, url_prefix="/api/items")

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        return send_from_directory('frontend/html', 'login.html')

    @app.route('/frontend/<path:path>')
    def serve_frontend(path):
        return send_from_directory('frontend', path)

    @app.route('/html/<path:path>')
    def serve_html(path):
        return send_from_directory('frontend/html', path)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)


@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Ressource nicht gefunden"}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Interner Serverfehler"}), 500
