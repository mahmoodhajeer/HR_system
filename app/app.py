from flask import Blueprint
from flask_restful import Api
from app.resource.CandidateResource import CandidateResource
from app.resource.ResumeResource import ResumeResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(CandidateResource, '/candidate')
api.add_resource(ResumeResource, '/resume')