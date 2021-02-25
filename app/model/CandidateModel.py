from app.model.database import Candidate, db


class CandidateModel(): 
    def create(self, data):
        new_candidate = Candidate(
            full_name = data['full_name'],
            date_of_birth = data['date_of_birth'],
            years_of_experience = data['years_of_experience'],
            department_ID = data['department_ID'],
            resume = data['resume']
        )
        db.session.add(new_candidate)
        db.session.commit()

        return new_candidate
    
    def getall(self):
        candidates =Candidate.query.all()
        return candidates

  