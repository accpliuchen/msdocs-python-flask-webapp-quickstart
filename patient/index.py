from flask import Blueprint, render_template
from flask import Flask
from flask import request
from flask import session
from flask_session import Session
from flask.views import View

import base64
import json
import util

from util.dbutil import AmanMySQL

patient_blueprint = Blueprint('patient', __name__)

@patient_blueprint.route("/patient")
def index():
    return "patient_blueprint"

@patient_blueprint.route('/patient_save', methods=['GET', 'POST'])
def patient_save():

    full_name =  request.form['full_name'] 
    medical_record_number = request.form['medical_record_number']
    dob= request.form['dob'] 

    age_Range =  request.form['age_Range'] 
    weight_range_t = request.form['weight_range_t']
    weight_range_g= request.form['weight_range_g'] 
    weight_range_r= request.form['weight_range_r']
    performance_status= request.form['performance_status'] 
    cancer_by_location= request.form['cancer_by_location'] 
    cancer_by_type= request.form['cancer_by_type']

    histopathologic_type =  request.form['histopathologic_type'] 
    histopathologic_tumor_grade = request.form['histopathologic_tumor_grade']
    staging_system_version= request.form['staging_system_version'] 
    classification= request.form['classification']
    primary_tumor= request.form['primary_tumor'] 
    regional_lymph_node= request.form['regional_lymph_node'] 
    distant_metastasis= request.form['distant_metastasis']


    estrogen_receptor_status =  request.form['estrogen_receptor_status'] 
    progesterone_receptor_status = request.form['progesterone_receptor_status']
    her2neu_status= request.form['her2neu_status'] 
    dimension_range= request.form['dimension_range']
    volume_range= request.form['volume_range'] 
    laterality= request.form['laterality'] 
    prior_treatment= request.form['prior_treatment']

    treatment_intent =  request.form['treatment_intent'] 
    treatment_setting = request.form['treatment_setting']
    roost_dose_modality= request.form['roost_dose_modality'] 
    additional_therapies= request.form['additional_therapies']
    type_of_therapy = request.form['type_of_therapy']

    timing_of_therapy= request.form['timing_of_therapy'] 
    tcp_outcomes= request.form['tcp_outcomes'] 
    end_point_primary= request.form['end_point_primary']
    end_point_secondary= request.form['end_point_secondary']


    local_control =  request.form['local_control'] 
    overall_survival = request.form['overall_survival']
    quality_of_life= request.form['quality_of_life'] 
    ntcp_outcomes_end_point_primary= request.form['ntcp_outcomes_end_point_primary']
    ntcp_outcomes_end_point_secondy= request.form['ntcp_outcomes_end_point_secondy'] 
    median_follow_up= request.form['median_follow_up'] 
    ntcp_outcomes_acute= request.form['ntcp_outcomes_acute']

    ntcp_outcomes_g1 =  request.form['ntcp_outcomes_g1'] 
    ntcp_outcomes_g2 = request.form['ntcp_outcomes_g2']
    ntcp_outcomes_g3= request.form['ntcp_outcomes_g3'] 
    ntcp_outcomes_g4= request.form['ntcp_outcomes_g4']
    ntcp_outcomes_g5= request.form['ntcp_outcomes_g5'] 
   

    modality =  request.form['modality'] 
    planing = request.form['planing']
    delivery= request.form['delivery'] 
    imaging= request.form['imaging']
    setup= request.form['setup'] 


    useDB = AmanMySQL()

    #modality,planing,delivery,imaging,setup
    #+modality+"','"+planing+"','"+imaging+"','"+setup+"'
    result=useDB.insert("insert into patients(full_name,medical_record_number,dob,age_Range,weight_range_t,weight_range_g,weight_range_r,performance_status,cancer_by_location,cancer_by_type,histopathologic_type,histopathologic_tumor_grade,staging_system_version,classification,primary_tumor,regional_lymph_node,distant_metastasis,estrogen_receptor_status,progesterone_receptor_status,her2neu_status,dimension_range,volume_range,laterality,prior_treatment,treatment_intent,treatment_setting,roost_dose_modality,additional_therapies,type_of_therapy,timing_of_therapy,tcp_outcomes,end_point_primary,end_point_secondary,local_control,overall_survival,quality_of_life,ntcp_outcomes_end_point_primary,ntcp_outcomes_end_point_secondy,median_follow_up,ntcp_outcomes_acute,ntcp_outcomes_g1,ntcp_outcomes_g2,ntcp_outcomes_g3,ntcp_outcomes_g4,ntcp_outcomes_g5,modality,planing,delivery,imaging,setup,createDateTime) values('"+full_name+"','"+medical_record_number+"','"+dob+"','"+age_Range+"','"+weight_range_t+"','"+weight_range_g+"','"+weight_range_r+"','"+performance_status+"','"+cancer_by_location+"','"+cancer_by_type+"','"+histopathologic_type+"','"+histopathologic_tumor_grade+"','"+staging_system_version+"','"+classification+"','"+primary_tumor+"','"+regional_lymph_node+"','"+distant_metastasis+"','"+estrogen_receptor_status+"','"+progesterone_receptor_status+"','"+her2neu_status+"','"+dimension_range+"','"+volume_range+"','"+laterality+"','"+prior_treatment+"','"+treatment_intent+"','"+treatment_setting+"','"+roost_dose_modality+"','"+additional_therapies+"','"+type_of_therapy+"','"+timing_of_therapy+"','"+tcp_outcomes+"','"+end_point_primary+"','"+end_point_secondary+"','"+local_control+"','"+overall_survival+"','"+quality_of_life+"','"+ntcp_outcomes_end_point_primary+"','"+ntcp_outcomes_end_point_secondy+"','"+median_follow_up+"','"+ntcp_outcomes_acute+"','"+ntcp_outcomes_g1+"','"+ntcp_outcomes_g2+"','"+ntcp_outcomes_g3+"','"+ntcp_outcomes_g4+"','"+ntcp_outcomes_g5+"','"+modality+"','"+planing+"','"+delivery+"','"+imaging+"','"+setup+"',NOW())")
    return json.dumps(result)

@patient_blueprint.route('/patient_load', methods=['GET', 'POST'])
def patient_load():
    useDB = AmanMySQL()
    sql = "select id,full_name,medical_record_number,dob,age_Range,weight_range_t,weight_range_g,weight_range_r,performance_status,cancer_by_location,cancer_by_type,histopathologic_type,histopathologic_tumor_grade,staging_system_version,classification,primary_tumor,regional_lymph_node,distant_metastasis,estrogen_receptor_status,progesterone_receptor_status,her2neu_status,dimension_range,volume_range,laterality,prior_treatment,treatment_intent,treatment_setting,roost_dose_modality,additional_therapies,type_of_therapy,timing_of_therapy,tcp_outcomes,end_point_primary,end_point_secondary,local_control,overall_survival,quality_of_life,ntcp_outcomes_end_point_primary,ntcp_outcomes_end_point_secondy,median_follow_up,ntcp_outcomes_acute,ntcp_outcomes_g1,ntcp_outcomes_g2,ntcp_outcomes_g3,ntcp_outcomes_g4,ntcp_outcomes_g5,modality,planing,delivery,imaging,setup from patients"

    getAll = useDB.get_all(sql)
    data=[]
    row_headers=useDB.get_all_headers("select id,full_name,medical_record_number,dob,age_Range,weight_range_t,weight_range_g,weight_range_r,performance_status,cancer_by_location,cancer_by_type,histopathologic_type,histopathologic_tumor_grade,staging_system_version,classification,primary_tumor,regional_lymph_node,distant_metastasis,estrogen_receptor_status,progesterone_receptor_status,her2neu_status,dimension_range,volume_range,laterality,prior_treatment,treatment_intent,treatment_setting,roost_dose_modality,additional_therapies,type_of_therapy,timing_of_therapy,tcp_outcomes,end_point_primary,end_point_secondary,local_control,overall_survival,quality_of_life,ntcp_outcomes_end_point_primary,ntcp_outcomes_end_point_secondy,median_follow_up,ntcp_outcomes_acute,ntcp_outcomes_g1,ntcp_outcomes_g2,ntcp_outcomes_g3,ntcp_outcomes_g4,ntcp_outcomes_g5,modality,planing,delivery,imaging,setup from patients")

    for result in getAll:
        data.append(dict(zip(row_headers,result)))
    
    json_data={"data":data}

    return json.dumps(json_data)