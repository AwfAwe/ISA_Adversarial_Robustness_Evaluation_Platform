from flask import Blueprint, jsonify, request
from sqlalchemy.orm import sessionmaker
import json

from src.util import state
from src.db import db

image = Blueprint('image', __name__)


@image.route('/change_image_name', methods=['GET', 'POST'])
def change_image_name():
    db_session = sessionmaker(bind=db)()

    try:
        image_info = json.loads(request.get_data())
        image_id = image_info['image_id']
        image_name = image_info['image_name']

        db_session.execute(
            'update image set image_name = \'%s\' '
            'where image_id = %s'
            % (image_name, image_id)
        )
        db_session.commit()
    except:
        db_session.close()
        jsonify({'state': state['UPDATE_IMAGE_FAIL']})

    db_session.close()
    return jsonify({'state': state['SUCCESS']})


@image.route('delete_image', methods=['GET', 'POST'])
def delete_image():
    db_session = sessionmaker(bind=db)()
    try:
        image_data = json.loads(request.get_data())
        image_id = image_data['image_id']
        db_session.execute(
            'delete from image '
            'where image_id = \'%s\''
            % image_id
        )
        db_session.commit()
    except:
        db_session.close()
        return jsonify({'state': state['DELETE_IMAGE_FAIL']})

    db_session.close()
    return jsonify({'state': state['SUCCESS']})