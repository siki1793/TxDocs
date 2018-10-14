import os
import urllib

basedir = os.path.abspath(os.path.dirname(__file__))

class Auth:
      CLIENT_ID = ('244606477390-np487sj3r07s5ve093inog7na84qfs31.apps.googleusercontent.com')
      CLIENT_SECRET = '9A4Wy-iKxBMiEdENHK3Yx1db'
      REDIRECT_URI = 'https://localhost:5000/gCallback'
      AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
      TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
      USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'

class Config:
      APP_NAME = "TxDocs"
      SECRET_KEY = os.environ.get("SECRET_KEY") or "somethingsecret"

# following should be as follows specially MONGO_URI and MONGO_DBNAME
class DevConfig(Config):
      DEBUG = True
      USER = urllib.quote('saikrishna1793.sk')
      PASSWORD = urllib.quote('Sai@17.m')
      MONGO_DBNAME = 'txdocs'
      MONGO_URI = 'mongodb://'+USER+':'+PASSWORD+'@ds121183.mlab.com:21183/txdocs'


class ProdConfig(Config):
      DEBUG = True
      USER = urllib.quote('saikrishna1793.sk')
      PASSWORD = urllib.quote('Sai@17.m')
      MONGO_DBNAME = 'txdocs'
      MONGO_URI = 'mongodb://'+USER+':'+PASSWORD+'@ds121183.mlab.com:21183/txdocs'


config = {
    "dev": DevConfig,
    "prod": ProdConfig,
    "default": DevConfig
}