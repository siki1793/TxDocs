from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask_login import LoginManager, login_required, login_user,logout_user, current_user, UserMixin
from config import config
app = Flask(__name__)

app.config.from_object(config['dev'])

print(app.config['MONGO_URI'])
mongo = PyMongo(app)

if __name__ == '__main__':
    app.run(debug=True)
