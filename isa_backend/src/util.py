from flask import session
import functools
import base64
import io


# 错误码
state = {
    'SUCCESS': 0,
    'ERROR': 1,
    'ADD_MODEL_FAIL': 2,
    'DELETE_MODEL_FAIL': 3,
    'UPDATE_MODEL_FAIL': 4,
    'GET_MODEL_FAIL': 5,
    'ADD_IMAGE_FAIL': 6,
    'DELETE_IMAGE_FAIL': 7,
    'UPDATE_IMAGE_FAIL': 8,
    'GET_IMAGE_FAIL': 9,
}
