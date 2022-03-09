import os
import re

class Config:
    '''
    General configuration parent class
    '''

    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = 'melonie'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://melonie:Access@localhost/pitchapp'

   #email configs
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
        
    '''
    
    SQLALCHEMY_DATABASE_URI='postgresql://vqlcuyilqymmcm:ce4d8595deff53944c124d815c209f0ce19852c5e0c935337fdcc021b9dda13e@ec2-3-231-254-204.compute-1.amazonaws.com:5432/d7un6qs7pu347l'
   
    
    


class DevConfig(Config):
    '''
    Development  configuration child class 

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://melonie:Access@localhost/pitch'
  

    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}