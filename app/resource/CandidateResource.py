from flask import request
from flask_restful import Resource
from app.model.CandidateModel import CandidateModel
from app.model.database import CandidateSchema
from marshmallow import ValidationError



candidates_schema = CandidateSchema(many=True)
candidate_schema = CandidateSchema()

class CandidateResource(Resource):
    def post(self):
        try:
            json_data = request.get_json(force=True)
        except :
            return{'status': 'fail', 'message': 'No input or not supported data provided'},400

        
        try:
            candidate_schema.load(json_data)
        except ValidationError as err:
            return { 'status': 'fail', 'message': err.messages}, 422

        
        
        candidate = CandidateModel()
        
        new_candidate = candidate.create(json_data)
        
        result = candidate_schema.dump(new_candidate)


        return { "status": 'success', 'data': result }, 201

    def get(self):
        try:
            admin = request.headers['X-ADMIN']
        except :
            return {'status': 'fail', 'message': 'No input or not supported data provided'},400
        
        if admin != '1':
            return {'status': 'fail', 'message': 'you have no access for this page'},401

        
        candidate = CandidateModel()
        candidates = candidate.getall()
        results = candidates_schema.dump(candidates)

        return {'status': 'success', 'data': results}, 200
            