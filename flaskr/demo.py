import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db
from werkzeug.exceptions import abort

bp = Blueprint('demo', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():

    # db = get_db()
    # posts = db.execute(
    #     'SELECT p.id, title, body, created, author_id, username'
    #     ' FROM post p JOIN user u ON p.author_id = u.id'
    #     ' ORDER BY created DESC'
    # ).fetchall()
    # Get image
    # image_path = 'img/sat_img.png'

    # getPrediction(predefined_geo_location_string):
    # get img for given predefined_geo_location_string (as a string eg. "stockholm")
    # *if needed: retrieve from db desired predefined coordinates for this geo location
    # process img
    # run prediction on img
    # colour img with RGB 
    # save img on local disk as img_predicted (overwrite or create new one)
    # return path_to_img_predicted

    if request.method == 'POST':
        location = request.form.get('locationFormSelect')
        print(location)
        if location is not None:
            path_to_img_predicted = 'img/algal_waste.png'
            img_path = url_for('static', filename=path_to_img_predicted)
            return render_template('demo/prediction.html', img_path=img_path)

    path_to_img_predicted = 'img/sat_img.png'
    img_path = url_for('static', filename=path_to_img_predicted)
    return render_template('demo/index.html', img_path=img_path)