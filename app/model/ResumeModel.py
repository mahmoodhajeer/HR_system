from werkzeug.utils import secure_filename
from config import resumes_dir
import os, datetime


class ResumeModel(): 
    def uploud(self, file):
        filename = secure_filename(file.filename)
        filename = str(datetime.datetime.now()) + filename
        file.save(os.path.join(resumes_dir, filename))

        return filename