import uuid
import datetime

from app.db.model.file import File


def save_new_file(data):
    my_file = File(**data).load()

    if not my_file.id:
        new_file = File(**{**data, **{
            'id': uuid.uuid4().hex.upper(),
            'created_on': datetime.datetime.utcnow()
        }})
        my_file = new_file

    my_file.name = data.get('name', None)
    my_file.description = data.get('description', None)
    my_file.modified_on = datetime.datetime.utcnow()

    if File().db().find_one({'_id': {'$ne': my_file.id}, 'name': my_file.name}):
        return {"status": 'fail', "message": 'File name already used'}, 409

    my_file.save()

    return {"status": "success", "message": "File saved"}, 201


def get_all_files():
    return File.get_all()

def get_a_file(file_id):
    my_file = File(**{'id': file_id}).load()

    if my_file.id:
        return my_file
    else:
        return {"status": "success", "message": "File not found."}, 404


