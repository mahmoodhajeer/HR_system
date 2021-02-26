from flask import request, send_from_directory
from flask_restful import Resource
from config import resumes_dir
import json


from app.model.ResumeModel import ResumeModel


class ResumeResource(Resource):
    def post(self):
        if 'file' not in request.files:
            return { "status": 'fail', 'message': 'No file part in the request'}, 400

        file = request.files['file']
        if file.filename == '' :
            return { "status": 'fail', 'message': 'No file selected for uploading'}, 400

        if not allowed_file(file.filename):
            return { "status": 'fail', 'message': 'not allowed file, just fdf or docx'}, 400
        
        resume_model = ResumeModel()
        file_name = resume_model.uploud(file)

        return { "status": 'success', 'data': file_name }, 201

    def get(filename):
        try:
            admin = request.headers['X-ADMIN']
        except :
            return {'status': 'fail', 'message': 'No input or not supported data provided'},400
        
        if admin != '1':
            return {'status': 'fail', 'message': 'you have no access for this page'},401

        args = request.args
        filename = args['filename']

        return send_from_directory(resumes_dir, filename, as_attachment=True),200

def allowed_file(filename):
    allowed_extenstion = set(['docx','pdf'])
    return '.' in filename and filename.split('.',1)[1].lower() in allowed_extenstion