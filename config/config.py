# config/config.py
class Config:
 
#Remote DB
    SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://sql10677641:'
        'jjzrttQIpK@sql10.freemysqlhosting.net/'
        'sql10677641'
    )
SQLALCHEMY_TRACK_MODIFICATIONS = False