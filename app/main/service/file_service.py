import uuid

from bson import ObjectId
from flask import  make_response

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
    return {"file_id":data}


def get_all_files():
    return File.get_all()

def get_a_file(file_id):
    resp = make_response(mongo.send_file(file_id))
    resp.headers.set('Content-Disposition', 'attachment', filename='converter.pdf')
    resp.headers.set('Content-Type', 'application/pdf')
    return resp

def delete_file(file_id):
    mongo.db['convertPDF'].delete_one({"_id": ObjectId(file_id)})
