import os


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost/HR_system?charset=utf8"

resumes_dir = basedir + "/app/resumes"
