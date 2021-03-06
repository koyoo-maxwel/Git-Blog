import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SENDER_EMAIL = 'koyoomaxwel@gmail.com'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://student:1209@localhost/blog'


   

class ProdConfig(Config):
    #SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_BROWN_URL")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://student:1209@localhost/blog'
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://student:1209@localhost/blog'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}    