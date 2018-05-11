import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_uploads import UploadSet, IMAGES, configure_uploads


# instantiate the db
db = SQLAlchemy()

def create_app():

    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # set up image uploading via flask-uploads
    photos = UploadSet('photos', IMAGES)
    app.config['UPLOADED_PHOTOS_DEST'] = '/static/'
    configure_uploads(app, photos)

    # register blueprints
    from project.api.views import albums_blueprint
    app.register_blueprint(albums_blueprint)

    return app
