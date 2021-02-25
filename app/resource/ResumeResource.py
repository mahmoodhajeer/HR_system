from flask import request
from flask_restful import Resource

from app.model.ResumeModel import ResumeModel


class ResumeResource(Resource):
    def post(self):
        if 'file' not in request.files:
            return { "status": 'fail', 'message': 'No file part in the request'}, 400

        file = request.files['file']
        if file.filename == '' :
            return { "status": 'fail', 'message': 'No file selected for uploading'}, 400
        
        resume_model = ResumeModel()
        file_name = resume_model.uploud(file)

        return { "status": 'success', 'data': file_name }, 201