from flask import request
from flask_restplus import Resource



from ..dto.file_dto import FileDto
from ..service.file_service import get_all_files, save_new_file, get_a_file, delete_file

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
    @api.expect(_file)
    def post(self):
        """Creates a new File """
        try:
            data = request.form['name']
            file = request.files["file"]
            return save_new_file(data=data,file=file)
        except Exception:
            {"status": 'fail', "message": 'Missing arguments'}, 409



@api.route('/<file_name>')
@api.param('file_name', 'The File name')
@api.response(404, 'File not found.')
class File(Resource):

    @api.doc('get a file')
    def post(self, file_name):
        """get a file given its identifier"""
        file = get_a_file(file_name)
        return file

    @api.doc('delete a file')
    def delete(self, file_name):
        """delete a file given its name"""
        try:
            delete_file(file_name)
            return {"status": 'success', "message": 'File deleted successfully'}, 201
        except Exception:
            return {"status": 'fail', "message": 'Missing file'}, 409



