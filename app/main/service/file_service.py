import io
import uuid

import base64
from io import BytesIO

import flask
from flask import send_file, make_response

from app.db.db import mongo

from app.db.model.file import File


def save_new_file(data,file):
    if data and file:
        status= "started"
        id = uuid.uuid4().hex.upper()
        new_file = File(**{**{'id': id}})
        mongo.save_file(data,file)
        new_file.name = data
        new_file.status = status
    else:
        return {"status": 'fail', "message": 'Enter a valid input'}

    if File().db().find_one({'_id': {'$ne': new_file.id}, 'name': new_file.name}):
        return {"status": 'fail', "message": 'File name already used'}, 409

    new_file.save()

    return {"file_name":data, "status": "success", "message": "File saved"}, 201


def get_all_files():
    return File.get_all()

def get_a_file(file_name):
    resp = make_response(mongo.send_file(file_name))
    resp.headers.set('Content-Disposition', 'attachment', filename='monpdf.pdf')
    resp.headers.set('Content-Type', 'application/pdf')
    #mon_pdf = mongo.send_file(file_name)
    return resp
