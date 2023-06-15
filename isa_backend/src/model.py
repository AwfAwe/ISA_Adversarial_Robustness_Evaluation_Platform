from flask import Blueprint, jsonify, request
from sqlalchemy.orm import sessionmaker
import json

from src.util import state
from src.db import db

aimodel = Blueprint('aimodel', __name__)


@aimodel.route('/change_aimodel_name', methods=['GET', 'POST'])
def change_aimodel_name():
    db_session = sessionmaker(bind=db)()

    try:
        aimodel_info = json.loads(request.get_data())
        aimodel_id = aimodel_info['aimodel_id']
        aimodel_name = aimodel_info['aimodel_name']

        db_session.execute(
            'update aimodel set aimodel_name = \'%s\' '
            'where aimodel_id = %s'
            % (aimodel_name, aimodel_id)
        )
        db_session.commit()
    except:
        db_session.close()
        jsonify({'state': state['UPDATE_MODEL_FAIL']})

    db_session.close()
    return jsonify({'state': state['SUCCESS']})


@aimodel.route('delete_aimodel', methods=['GET', 'POST'])
def delete_aimodel():
    db_session = sessionmaker(bind=db)()
    try:
        aimodel_data = json.loads(request.get_data())
        aimodel_id = aimodel_data['aimodel_id']
        db_session.execute(
            'delete from aimodel '
            'where aimodel_id = \'%s\''
            % aimodel_id
        )
        db_session.commit()
    except:
        db_session.close()
        return jsonify({'state': state['DELETE_MODEL_FAIL']})

    db_session.close()
    return jsonify({'state': state['SUCCESS']})