from flask_restplus import Namespace, fields


class FileDto:
    api = Namespace('file', description='file related operations')
    file = api.model('file', {
        'name': fields.String(required=True, description='file name'),
    })