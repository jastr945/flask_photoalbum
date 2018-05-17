from flask import Flask, jsonify, Blueprint, request, render_template, redirect, session, url_for
from project.api.models import Album, Image
from project import db
from sqlalchemy import exc
import datetime
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class
from flask_cors import CORS
import json
from urllib.request import urlopen
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage


# creating an instance of an app and configuring Flask-Uploads
app = Flask(__name__)
CORS(app)
app.config['UPLOADED_PHOTOS_DEST'] = 'static'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app, 32 * 1024 * 1024) # limits uploaded images to 32 megabytes

# creating a blueprint
albums_blueprint = Blueprint('albums', __name__)

# storage for Google access token
storage = Storage('credentials_file')


@albums_blueprint.route('/', methods=['GET', 'POST'])
def index():
    """Index page with each user's albums listed. If not signed in, display default albums."""
    credentials = storage.get()
    if credentials and len(credentials.id_token['email']) > 0:
        albums = Album.query.filter_by(user_email=credentials.id_token['email'])
    else:
        albums = Album.query.filter_by(user_email="example@example.com")
    # if request.method == 'POST':
    #     title = request.form['title']
    #     description = request.form['description']
    #     album = Album(title=title, description=description)
    #     album.images = photos_list
    #     db.session.add(album)
    #     db.session.commit()
    return render_template('index.html', albums=albums)


@albums_blueprint.route('/google', methods=['POST'])
def add_code():
    """Receiving the access code from the Client and storing it"""
    access_code = json.loads(request.data)['headers']['Authorization'] # obtaining the access code from Client
    if not access_code:
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        return jsonify(response_object), 400
    flow = OAuth2WebServerFlow(client_id='418257197191-75oafj28gkn84pj7ebgvt54av0vtt7br.apps.googleusercontent.com',
                               client_secret='WFVzMZNMObdCcc1WjD-ifALs',
                               scope='profile',
                               redirect_uri='http://slider.mee.how:9000')
    credentials = flow.step2_exchange(access_code[7:]) # exchanging access code for token
    storage.put(credentials)
    response_object = {
        'status': 'success',
        'message': 'Login credentials were obtained!'
    }
    return jsonify(response_object), 200


@albums_blueprint.route('/googleauthorized', methods=['GET'])
def authorized():
    """Decoding the access code and grabbing user data"""
    credentials = storage.get()
    if credentials:
        email = credentials.id_token['email']
        pic = credentials.id_token['picture']
        response_object = {
            'status': 'success',
            'data': {
                'email': email,
                'pic': pic
            }
        }
    else:
        response_object = {
            'status': 'success',
            'data': {
                'email': '',
                'pic': ''
            }
        }
    return jsonify(response_object), 200


@albums_blueprint.route('/googlelogout', methods=['GET'])
def remove_user():
    """Google logout"""
    credentials = storage.get()
    if credentials:
        storage.delete()
        response_object = {
            'status': 'success',
            'data': {
                'email': '',
                'pic': ''
            }
        }
    return jsonify(response_object), 200


@albums_blueprint.route('/albums', methods=['POST'])
def add_album():
    credentials = storage.get()
    if len(credentials.id_token['email']) > 0:
        post_data = request.form
        if not post_data:
            response_object = {
                'status': 'fail',
                'message': 'Invalid payload.'
            }
            return jsonify(response_object), 400

        title = request.form['title']
        try:
            album = Album.query.filter_by(title=title).first()
            if not album:
                description = request.form['description']
                new_album = Album(title=title, description=description, user_email=credentials.id_token['email'])
                new_album.images=[]
                for i in request.files.getlist('photos'):
                    filename = photos.save(i) # saving images via Flask-Uploads
                    img_url = photos.url(filename) # extracting image url with Flask-Uploads
                    new_image = Image(name=filename, url=img_url)
                    new_album.images.append(new_image) # One-to-many relationship instantiation
                db.session.add(new_album)
                db.session.commit()
                response_object = {
                    'status': 'success',
                    'message': f'{title} was added!'
                }
                return jsonify(response_object), 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'Sorry. That title already exists.'
                }
                return jsonify(response_object), 400
        except (exc.IntegrityError, ValueError) as e:
            db.session().rollback()
            response_object = {
                'status': 'fail',
                'message': 'Invalid payload.'
            }
            return jsonify(response_object), 400
    else:
        response_object = {
            'status': 'fail',
            'message': 'Unauthorized access. Please log in.'
        }
        return jsonify(response_object), 403

@albums_blueprint.route('/albums', methods=['GET'])
def get_all_albums():
    """Get all albums"""
    credentials = storage.get()
    if credentials and len(credentials.id_token['email']) > 0:
        albums = Album.query.filter_by(user_email=credentials.id_token['email'])
    else:
        albums = Album.query.filter_by(user_email="example@example.com")
    # albums = Album.query.order_by(Album.created_at.desc()).all()
    albums_list = []
    for album in albums:
        album_object = {
            'id': album.id,
            'title': album.title,
            'description': album.description,
            'created_at': album.created_at.isoformat(),
            'images': [str(i.url) for i in album.images] # sending image url to React
        }
        albums_list.append(album_object)
    response_object = {
        'status': 'success',
        'data': {
            'albums': albums_list
        }
    }
    return jsonify(response_object), 200


@albums_blueprint.route('/albums/<album_id>', methods=['GET'])
def get_single_album(album_id):
    """Get single album details"""
    response_object = {
        'status': 'fail',
        'message': 'Album does not exist'
    }
    try:
        album = Album.query.filter_by(id=int(album_id)).first()
        if not album:
            return jsonify(response_object), 404
        else:
            response_object = {
                'status': 'success',
                'data': {
                  'title': album.title,
                  'description': album.description,
                  'created_at': album.created_at.isoformat(),
                  'images': [str(i.url) for i in album.images] # sending image url to React
                }
            }
            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404


@albums_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    """Just a test"""
    return jsonify({
        'status': 'success',
        'message': 'kittykats!'
    })
