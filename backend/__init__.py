from flask import Flask
from backend.config import Config
from backend.routes.main_routes import main

def create_app():
    app = Flask(__name__)

    # 설정 적용
    app.config.from_object(Config)

    # Blueprint 등록
    app.register_blueprint(main)

    return app