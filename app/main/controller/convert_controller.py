from flask import request
from flask_restplus import Resource



from ..dto.split_dto import SplitDto
from ..service.convert_service import split_file

api = SplitDto.api
_split = SplitDto.file


@api.route('/split')
class SplitFile(Resource):
    @api.doc('Split file')
    @api.expect(_split)
    def post(self):
        """Split file"""
        file_name = request.form['name']
        start_page = request.form['start_page']
        end_page = request.form['end_page']
        file = request.files["file"]
        return split_file(start_page,end_page,file,file_name)



