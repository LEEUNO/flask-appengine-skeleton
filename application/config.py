import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'df32tgi32(=vfT2G!'
    DEBUG = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @classmethod
    def init_app(cls, app):
        print "init app..."
        
        if os.getenv('SERVER_SOFTWARE') \
                and os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/'):
            # deploy data base URI
            cls.SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@127.0.0.1:3306/<schema_name>' \
                                          '?unix_socket=/cloudsql/<cloud_sql_instance_id>?charset=utf8'
        else:
            print "local!!!!"
            # dev_appserver.py or appengine launcher
            cls.SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://<username>:<password>@<ip_addresss>/<schema_name>'

        app.config.from_object(cls)
