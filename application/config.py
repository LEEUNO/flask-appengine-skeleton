import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'df32tgi32(=vfT2G!'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///main?instance=flask-rest-api:jh?charset=utf8'

    @staticmethod
    def init_app(app):
        pass
