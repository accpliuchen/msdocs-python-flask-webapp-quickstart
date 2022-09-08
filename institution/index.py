from flask import Blueprint, render_template
from flask import Flask
from flask import request
from flask.views import View
# from flaskext.mysql import MySQL

import json
# import pymysql
# import MySQLdb
# from config import db_conf
# import app
import util
from util.dbutil import AmanMySQL

institution_blueprint = Blueprint('institution', __name__)

@institution_blueprint.route("/institution")
def index():
    return "institution111"


@institution_blueprint.route("/institutionhello")
def hello():
    language = "Python"
    company = "GeeksForGeeks"
    Itemid = 1
    price = 0.00
 
    # Create Dictionary
    value = {
        "language": language,
        "company": company,
        "Itemid": Itemid,
        "price": price
    }
    
    return json.dumps(value)


@institution_blueprint.route('/institution_load', methods=['GET', 'POST'])
def institution_requestLoad():
    useDB = AmanMySQL()
    sql = "select Id,InstitutionCode,InstitutionName from Institution"
    getAll = useDB.get_all(sql)
    print(json.dumps(getAll))
    return json.dumps(getAll)

@institution_blueprint.route('/institution_delete', methods=['GET', 'POST'])
def institution_requestDelete():
   useDB = AmanMySQL()
   id = request.args.get('id')

   result = useDB.delete("delete from Institution where id='"+id+"'")
   return json.dumps(result)

@institution_blueprint.route('/institution_save', methods=['GET', 'POST'])
def institution_save():

    #institutioncode=
    code =  request.form['institutioncode'] # code is empty
    name = request.form['institutionname'] # name is empty

    useDB = AmanMySQL()
    sql = "select Id,InstitutionCode,InstitutionName from Institution where InstitutionCode='"+code+"'"
    getOne = useDB.get_one(sql)

    if getOne is not None:
       return json.dumps(0)
    else:
       result=useDB.insert("insert into Institution(InstitutionCode,InstitutionName,CreateTime) values('"+code+"','"+name+"',NOW())")
       return json.dumps(result)


@institution_blueprint.route('/institution_edit', methods=['GET', 'POST'])
def institution_edit():

    #institutioncode=
    code = request.form['institutioncode']  # code is empty
    name = request.form['institutionname']  # name is empty
    id = request.form['id']  # name is empty

    print(code)
    print(name)
    print(id)

    useDB = AmanMySQL()

    result=useDB.update("update Institution set  InstitutionCode='"+code+"',InstitutionName='"+name+"' where id="+id+" ")

    print('result value is '+ str(result))
    return json.dumps(result)
