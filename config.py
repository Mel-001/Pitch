import os
import re

class Config:
    '''
    General configuration parent class
    '''

    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = 'melonie'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://melonie:Access@localhost/pitch'

   


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
        
    '''
    
   
   
    
    


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