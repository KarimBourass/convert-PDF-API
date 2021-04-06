import uuid

from PyPDF2 import PdfFileWriter, PdfFileReader

from app.db.db import mongo
from app.db.model.file import File


def split_file(start_page,end_page,file,file_name):
    if start_page and end_page and file:
        #id = uuid.uuid4().hex.upper()
        #new_file = File(**{**{'id': id}})
        input_pdf = PdfFileReader(file)
        output = PdfFileWriter()
        for page in range(int(start_page)-1, int(end_page)):
            output.addPage(input_pdf.getPage(page))
        with open("static/splited.pdf", "wb") as output_stream:
            output.write(output_stream)
    myFile = open("static/splited.pdf", "rb")
    mongo.save_file(file_name, myFile)
    return {"file_id":file_name}



