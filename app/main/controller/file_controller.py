from flask import request
from flask_restplus import Resource

from ..dto.file_dto import FileDto
from ..service.file_service import get_all_files, save_new_file, get_a_file

api = FileDto.api
_file = FileDto.file


@api.route('/')
class FileList(Resource):
    @api.doc('list_of_registered_files')
    @api.marshal_list_with(_file, envelope='data')
    def get(self):
        """List all registered files"""
        return get_all_files()

    @api.response(201, 'File successfully created.')
    @api.doc('create a new File')
    @api.expect(_file, validate=True)
    def post(self):
        """Creates a new File """
        data = request.json
        return save_new_file(data=data)
    
@api.route('/<file_id>')
@api.param('file_id', 'The File identifier')
@api.response(404, 'File not found.')
class File(Resource):

    @api.doc('get a file')
    @api.marshal_with(_file)
    def get(self, file_id):
        """get a file given its identifier"""
        file = get_a_file(file_id)
        if not file:
            api.abort(404)
        else:
            return file