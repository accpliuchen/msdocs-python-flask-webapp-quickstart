from flask import Blueprint, render_template
from flask import Flask
from flask import request
from flask import session
# from flask_session import Session
from flask.views import View

import base64
import json
import util

from util.dbutil import AmanMySQL

users_blueprint = Blueprint('users', __name__)



@users_blueprint.route('/first', methods=['GET', 'POST'])
def first():
    session['this_one'] = 'hello'
    return 'Hello was saved into session[this_one].'


@users_blueprint.route('/second', methods=['GET', 'POST'])
def second():
    return 'Value inside session[this_one] is {}.'.format(session['this_one'])

@users_blueprint.route("/users")
def index():
    return "user index"

# @users_blueprint.before_request
# def auth(): session['access'] = 'Admin'

@users_blueprint.route('/users_register', methods=['GET', 'POST'])
def users_register():

    username =  request.form['username'] # username is empty
    password = request.form['password'] # password is empty
    lastname= request.form['lastname'] # lastname is empty
    firstname= request.form['firstname'] # firstname is empty
    country= request.form['country'] # country is empty
    email= request.form['email'] # email is empty

    useDB = AmanMySQL()

    password_bytes = password.encode('ascii')
    base64_bytes = base64.b64encode(password_bytes)
    password = base64_bytes.decode('ascii')

    sql = "select Id from users where UserName='"+username+"' and email='"+email+"' "
    getOne = useDB.get_one(sql)

    if getOne is not None:
      return json.dumps(0)
    else:
      result=useDB.insert("insert into users(UserName,Password,LastName,FirstName,Country,Email,Type,status,CreateTime) values('"+username+"','"+password+"','"+lastname+"','"+firstname+"','"+country+"','"+email+"','0','inactive',NOW())")
      return json.dumps(1)

@users_blueprint.route('/users_login', methods=['POST'])
def users_login():
    username =  request.form['username'] # username is empty
    password = request.form['password'] # password is empty

    useDB = AmanMySQL()

    password_bytes = password.encode('ascii')
    base64_bytes = base64.b64encode(password_bytes)
    password = base64_bytes.decode('ascii')

    # sql = "select Id,UserName,LastName,FirstName,Email,status from users where UserName='"+username+"' and password='"+password+"'  and status='active' "
    # getOne = useDB.get_one(sql)

    # if getOne is not None:

    #    return json.dumps(0)
    # else:
    #    return json.dumps(1)

    useDB = AmanMySQL()
    sql = "select Id,UserName,LastName,FirstName,Email,type from users where UserName='"+username+"' and password='"+password+"'  and status='active'"

    getAll = useDB.get_all(sql)
    data=[]
    row_headers=useDB.get_all_headers("select Id,UserName,LastName,FirstName,Email,type from users where UserName='"+username+"' and password='"+password+"'  and status='active' ")

    for result in getAll:
        data.append(dict(zip(row_headers,result)))

    json_data={"data":data}

    return json.dumps(json_data)

@users_blueprint.route('/users_save', methods=['GET', 'POST'])
def users_save():
    username =  request.form['username']
    password = request.form['password']
    lastname= request.form['lastname']
    firstname= request.form['firstname']
    country= request.form['country']
    email= request.form['email']
    type= request.form['type']

    useDB = AmanMySQL()

    result=useDB.insert("insert into users(UserName,Password,LastName,FirstName,Country,Email,Type,status,CreateTime) values('"+username+"','"+password+"','"+lastname+"','"+firstname+"','"+country+"','"+email+"','"+type+"','active',NOW())")
    return json.dumps(result)


@users_blueprint.route('/user_edit', methods=['GET', 'POST'])
def user_edit():

    id = request.form['id']
    email = request.form['email']
    password = request.form['password']

    useDB = AmanMySQL()

    password_bytes = password.encode('ascii')
    base64_bytes = base64.b64encode(password_bytes)
    password = base64_bytes.decode('ascii')

    result=useDB.update("update users set Email='"+email+"',password='"+password+"' where id="+id+" ")
    return json.dumps(result)


@users_blueprint.route('/user_update_status', methods=['GET', 'POST'])
def user_update_status():

    id = request.form['id']
    user_status = request.form['user_status']

    useDB = AmanMySQL()

    result=useDB.update("update users set  status='"+user_status+"' where id="+id+" ")
    return json.dumps(result)

@users_blueprint.route('/user_load', methods=['GET', 'POST'])
def user_load():
    useDB = AmanMySQL()
    sql = "select Id,UserName,LastName,FirstName,Email,status from users"

    getAll = useDB.get_all(sql)
    data=[]
    row_headers=useDB.get_all_headers("select Id,UserName,LastName,FirstName,Email,status from users")

    for result in getAll:
        data.append(dict(zip(row_headers,result)))

    json_data={"data":data}

    return json.dumps(json_data)


