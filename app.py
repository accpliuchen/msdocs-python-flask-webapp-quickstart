from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, abort

from views.index import index_blueprint
from news.index import news_blueprint
from institution.index import institution_blueprint
from users.index import users_blueprint
from protocol.index import protocol_blueprint
from patient.index import patient_blueprint
from match.index import match_blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'secret-key'
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(index_blueprint)
app.register_blueprint(news_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(institution_blueprint)
app.register_blueprint(protocol_blueprint)
app.register_blueprint(patient_blueprint)
app.register_blueprint(match_blueprint)

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()