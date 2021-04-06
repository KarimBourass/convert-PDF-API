from flask_restplus import Namespace, fields

class SplitDto:
    api = Namespace('split', description='split related operations')
    file = api.model('split', {
        'start_page': fields.String(required=True, description='file start_page'),
        'end_page': fields.String(required=True, description='file end_page'),
    })

