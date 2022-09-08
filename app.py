# from datetime import datetime
# from flask import Flask, render_template, request, redirect, url_for, send_from_directory
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#    print('Request for index page received')
#    return render_template('index.html')
#
# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')
#
# @app.route('/hello', methods=['POST'])
# def hello():
#    name = request.form.get('name')
#
#    if name:
#        print('Request for hello page received with name=%s' % name)
#        return render_template('hello.html', name = name)
#    else:
#        print('Request for hello page received with no name or blank name -- redirecting')
#        return redirect(url_for('index'))
#
#
# if __name__ == '__main__':
#    app.run()


from flask import Flask, redirect, url_for, request, abort

from news.index import news_blueprint
from institution.index import institution_blueprint
from users.index import users_blueprint
from protocol.index import protocol_blueprint
from patient.index import patient_blueprint
from match.index import match_blueprint

# from flaskext.mysql import MySQL
# # from config import db_conf
# # import config
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

#mysql = MySQL()

application.config['SECRET_KEY'] = 'secret-key'
application.config['CORS_HEADERS'] = 'Content-Type'

application.config['MYSQL_DATABASE_USER'] = 'root'
application.config['MYSQL_DATABASE_PASSWORD'] = '123456'
application.config['MYSQL_DATABASE_DB'] = 'roytuts'
application.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(application)

application.register_blueprint(news_blueprint)
application.register_blueprint(users_blueprint)
application.register_blueprint(institution_blueprint)
application.register_blueprint(protocol_blueprint)
application.register_blueprint(patient_blueprint)
application.register_blueprint(match_blueprint)