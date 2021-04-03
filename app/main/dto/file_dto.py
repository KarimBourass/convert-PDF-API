from flask_restplus import Namespace, fields, reqparse
from werkzeug.datastructures import FileStorage

upload_parser = reqparse.RequestParser()
upload_parser.add_argument('file', location='files', type=FileStorage, required=True)



class FileDto:
    api = Namespace('file', description='file related operations')
    file = api.model('file', {
        'name': fields.String(required=True, description='file name'),
        'status': fields.String(required=True, description='file status'),
    })

