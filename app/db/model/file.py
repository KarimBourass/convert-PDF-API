from app.db.document import Document


class File(Document):
    __TABLE__ = "files"

    id = None
    name = None
    status = None
