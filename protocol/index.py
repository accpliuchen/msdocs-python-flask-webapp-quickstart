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

protocol_blueprint = Blueprint('protocol', __name__)

@protocol_blueprint.route("/protocol")
def index():
    return "protocol_blueprint"

# @users_blueprint.route('/protocol_example', methods=['GET', 'POST'])
# def protocol_example():
#     age_Range =  request.form['age_Range'] 
#     weight_range_t = request.form['weight_range_t']
#     weight_range_g= request.form['weight_range_g'] 
#     weight_range_r= request.form['weight_range_r']
#     performance_status= request.form['performance_status'] 
#     cancer_by_location= request.form['cancer_by_location'] 
#     cancer_by_type= request.form['cancer_by_type']

#     histopathologic_type =  request.form['histopathologic_type'] 
#     histopathologic_tumor_grade = request.form['histopathologic_tumor_grade']
#     staging_system_version= request.form['staging_system_version'] 
#     classification= request.form['classification']
#     primary_tumor= request.form['primary_tumor'] 
#     regional_lymph_node= request.form['regional_lymph_node'] 
#     distant_metastasis= request.form['distant_metastasis']


#     username =  request.form['estrogen_receptor_status'] 
#     password = request.form['progesterone_receptor_status']
#     lastname= request.form['her2neu_status'] 
#     firstname= request.form['dimension_range']
#     country= request.form['volume_range'] 
#     email= request.form['laterality'] 
#     types= request.form['prior_treatment']



#     treatment_intent =  request.form['treatment_intent'] 
#     treatment_setting = request.form['treatment_setting']
#     roost_dose_modality= request.form['roost_dose_modality'] 
#     additional_therapies= request.form['additional_therapies']
#     timing_of_therapy= request.form['timing_of_therapy'] 
#     tcp_outcomes= request.form['tcp_outcomes'] 
#     end_point_primary= request.form['end_point_primary']
#     end_point_secondary= request.form['end_point_secondary']


#     local_control =  request.form['local_control'] 
#     overall_survival = request.form['overall_survival']
#     quality_of_life= request.form['quality_of_life'] 
#     ntcp_outcomes_end_point_primary= request.form['additional_therapies']
#     ntcp_outcomes_end_point_secondy= request.form['timing_of_therapy'] 
#     median_follow_up= request.form['tcp_outcomes'] 
#     ntcp_outcomes_acute= request.form['end_point_primary']

#     ntcp_outcomes_g1 =  request.form['ntcp_outcomes_g1'] 
#     ntcp_outcomes_g2 = request.form['ntcp_outcomes_g2']
#     ntcp_outcomes_g3= request.form['ntcp_outcomes_g3'] 
#     ntcp_outcomes_g4= request.form['ntcp_outcomes_g4']
#     ntcp_outcomes_g5= request.form['ntcp_outcomes_g5'] 
   

#     modality =  request.form['modality'] 
#     planing = request.form['planing']
#     delivery= request.form['delivery'] 
#     imaging= request.form['imaging']
#     setup= request.form['setup'] 

#     useDB = AmanMySQL()

#     result=useDB.insert("insert into protocols(age_Range,weight_range_t,weight_range_g,weight_range_r,performance_status,cancer_by_location,cancer_by_type,histopathologic_type,histopathologic_tumor_grade,staging_system_version,classification,primary_tumor,regional_lymph_node,distant_metastasis,estrogen_receptor_status,progesterone_receptor_status,her2neu_status,dimension_range,volume_range,laterality,prior_treatment,treatment_intent,treatment_setting,roost_dose_modality,additional_therapies,type_of_therapy,timing_of_therapy,tcp_outcomes,end_point_primary,end_point_secondary,local_control,overall_survival,quality_of_life,ntcp_outcomes_end_point_primary,ntcp_outcomes_end_point_secondy,median_follow_up,ntcp_outcomes_acute,ntcp_outcomes_g1,ntcp_outcomes_g2,ntcp_outcomes_g3,ntcp_outcomes_g4,ntcp_outcomes_g5,modality,planing,delivery,imaging,setup,createDateTime) values('"+age_Range+"','"+weight_range_t+"','"+weight_range_g+"','"+weight_range_r+"','"+performance_status+"','"+cancer_by_location+"','"+cancer_by_type+"','"+histopathologic_type+"','"+histopathologic_tumor_grade+"','"+staging_system_version+"','"+classification+"','"+primary_tumor+"','"+regional_lymph_node+"','"+distant_metastasis+"','"+estrogen_receptor_status+"','"+progesterone_receptor_status+"','"+her2neu_status+"','"+dimension_range+"','"+volume_range+"','"+laterality+"','"+prior_treatment+"','"+treatment_intent+"','"+treatment_setting+"','"+roost_dose_modality+"','"+additional_therapies+"','"+type_of_therapy+"','"+timing_of_therapy+"','"+tcp_outcomes+"','"+end_point_primary+"','"+end_point_secondary+"','"+local_control+"','"+overall_survival+"','"+quality_of_life+"','"+ntcp_outcomes_end_point_primary+"','"+ntcp_outcomes_end_point_secondy+"','"+median_follow_up+"','"+ntcp_outcomes_g1+"','"+ntcp_outcomes_g2+"','"+ntcp_outcomes_g3+"','"+ntcp_outcomes_g4+"','"+modality+"','"+planing+"','"+imaging+"','"+setup+"',NOW())")
#     return json.dumps(result)

@protocol_blueprint.route('/protocol_save', methods=['GET', 'POST'])
def protocol_save():

    study_name =  request.form['study_name'] 
    protocol_name = request.form['protocol_name']
    publish_date= request.form['publish_date'] 
    study_type= request.form['study_type']
    analysis_type= request.form['analysis_type'] 
    number_of_patients= request.form['number_of_patients'] 
    study_institution= request.form['study_institution']

    print("part1")

    country_of_study =  request.form['country_of_study'] 
    publication_unique_id = request.form['publication_unique_id']
    doi= request.form['doi'] 
  
    weight_range_n= request.form['weight_range_n'] 

    age_range = request.form.getlist('age_range')


    weight_range_t = request.form.getlist('weight_range_t')
    weight_range_m = request.form.getlist('weight_range_m')

    performance_status= request.form.getlist('performance_status')

    age_range_data=""
    weight_range_t_data=""
    weight_range_m_data=""
    performance_status_data=""

    for age in age_range:
        age_range_data+=age+";"

    for range_t in weight_range_t:
        weight_range_t_data+=range_t+";"

    for range_m in weight_range_m:
        weight_range_m_data+=range_m+";"

    for performances in performance_status:
        performance_status_data+=performances+";"

    cancer_by_location= request.form['cancerbyLocation'] 
    cancer_by_type= request.form['cancerbyType']

    print("part3")

    histopathologic_type =   request.form.getlist('histopathologic_type')
    histopathologic_tumor_grade = request.form['histopathologic_tumor_grade']
    staging_system_version= request.form['staging_system_version'] 

    histopathologic_type_data=""
    for histopathologic_types in histopathologic_type:
        histopathologic_type_data+=histopathologic_types+";"

    print("part4")

    classification= request.form.getlist('classification')
    classification_data=""
    for classifications in classification:
        classification_data+=classifications+";"

    primary_tumor= request.form.getlist('primary_tumor')

    primary_tumor_data=""
    for primary_tumors in primary_tumor:
        primary_tumor_data+=primary_tumors+";"

    regional_lymph_node= request.form.getlist('regional_lymph_node')
    regional_lymph_data=""
    for regional_lymphs in regional_lymph_node:
        regional_lymph_data+=regional_lymphs+";"


    distant_metastasis= request.form.getlist('distant_metastasis')
    distant_metastasis_data=""
    for distant_metastasises in distant_metastasis:
        distant_metastasis_data+=distant_metastasises+";"

    print("part5")

    estrogen_receptor_status= request.form['estrogen_receptor_status']
    progesterone_receptor_status= request.form['progesterone_receptor_status'] 
    her2neu_status= request.form['her2neu_status'] 
    dimension_range= request.form['dimension_range']

    print("part6")

    volume_range =  request.form['volume_range'] 
    laterality = request.form['laterality']

    prior_treatment= request.form.getlist('prior_treatment')
    prior_treatment_data=""
    for prior_treatments in prior_treatment:
        prior_treatment_data+=prior_treatments+";"

    treatment_intent= request.form['treatment_intent']
    treatment_setting= request.form['treatment_setting'] 
    base_dose_modality= request.form['base_dose_modality'] 
    additional_therapies= request.form['additional_therapies']

    type_of_therapy= request.form.getlist('type_of_therapy')
    type_of_therapy_data=""
    for type_of_therapies in type_of_therapy:
        type_of_therapy_data+=type_of_therapies+";"

    print("part8")

    timing_of_therapy =  request.form['timing_of_therapy'] 
    tcp_outcomes = request.form['tcp_outcomes']
    end_point_primary= request.form['end_point_primary'] 
    end_point_secondary= request.form['end_point_secondary']
    local_control= request.form['local_control'] 
    overall_survival= request.form['overall_survival'] 
    quality_of_life= request.form['quality_of_life']

    print("part9")

    ntcp_outcomes_end_point_primary =  request.form['ntcp_outcomes_end_point_primary'] 
    ntcp_outcomes_end_point_secondary = request.form['ntcp_outcomes_end_point_secondary']
    median_follow_up= request.form['median_follow_up'] 
    acute= request.form['acute']

    print("part10")

    g1 = request.form['g1'] 
    g2 = request.form['g2']
    g3 = request.form['g3'] 
    g4 = request.form['g4']
    g5 = request.form['g5'] 

    print("part11")

    regiment_treatment_intent =  request.form['regiment_treatment_intent'] 
    regiment_treatment_setting = request.form['regiment_treatment_setting']
    base_dose_fraction= request.form['base_dose_fraction'] 
    boost_dose_by_modality= request.form['boost_dose_by_modality']
    regiment_additional_therapies= request.form['regiment_additional_therapies']

    print("part12")

    regiment_type_of_therapy =  request.form.getlist('regiment_type_of_therapy')
    regiment_type_of_therapy_data=""
    for regiment_type_of_therapies in regiment_type_of_therapy:
        regiment_type_of_therapy_data+=regiment_type_of_therapies+";"

    regiment_timing_of_therapy = request.form['regiment_timing_of_therapy']
    regiment_tcp_outcomes= request.form['regiment_tcp_outcomes'] 
    regiment_end_points_primary= request.form['regiment_end_points_primary']
    regiment_end_points_secondary= request.form['regiment_end_points_secondary'] 

 
    print("part13")

    media_follow_up_local_control =  request.form['media_follow_up_local_control'] 
    media_follow_up_overall_survival = request.form['media_follow_up_overall_survival']
    media_follow_up_quality_of_life= request.form['media_follow_up_quality_of_life'] 
    media_ntcp_outcomes_end_point_primary= request.form['media_ntcp_outcomes_end_point_primary']
    media_ntcp_outcomes_end_point_secondy= request.form['media_ntcp_outcomes_end_point_secondy'] 
    media_ntcp_outcomes_media_follow_up= request.form['media_ntcp_outcomes_media_follow_up'] 

 
    print("part14")

    ntcp_outcomes_acute =  request.form['ntcp_outcomes_acute'] 
    ntcp_media_g1 = request.form['ntcp_media_g1']
    ntcp_media_g2= request.form['ntcp_media_g2'] 
    ntcp_media_g3= request.form['ntcp_media_g3']
    ntcp_media_g4= request.form['ntcp_media_g4'] 
    ntcp_media_g5= request.form['ntcp_media_g5'] 

    print("part15")

    treatment_techniques =  request.form.getlist('treatment_techniques')  
    treatment_techniques_data=""
    for treatment_techniques_result in treatment_techniques:
        treatment_techniques_data+=treatment_techniques_result+";"

    planing = request.form.getlist('planing')
    planing_data=""
    for planing_result in planing:
        planing_data+=planing_result+";"

    delivery= request.form['delivery'] 
    delivery_data=""
    for delivery_result in delivery:
        delivery_data+=delivery+";"

    imaging= request.form.getlist('imaging')
    imaging_data=""
    for imaging_result in imaging:
        imaging_data+=imaging_result+";"

    setup= request.form.getlist('setup')
    setup_data=""
    for setup_result in setup:
        setup_data+=setup_result+";"

    key_conclusion= request.form['key_conclusion'] 

    print("part16")
    useDB = AmanMySQL()

    #,regiment_treatment_intent,regiment_treatment_setting,base_dose_fraction,boost_dose_by_modality,regiment_additional_therapies,regiment_type_of_therapy,regiment_timing_of_therapy,regiment_tcp_outcomes,regiment_end_points_primary,regiment_end_points_secondary,media_follow_up_local_control,media_follow_up_overall_survival,media_follow_up_quality_of_life,media_ntcp_outcomes_end_point_primary,media_ntcp_outcomes_end_point_secondy,media_ntcp_outcomes_media_follow_up,ntcp_outcomes_acute,ntcp_media_g1,ntcp_media_g2,ntcp_media_g3,ntcp_media_g4,ntcp_media_g5,treatment_techniques,planing,delivery,imaging,setup,key_conclusion,
    #,'"+regiment_treatment_intent+"','"+regiment_treatment_setting+"','"+base_dose_fraction+"','"+boost_dose_by_modality+"','"+regiment_additional_therapies+"','"+regiment_type_of_therapy+"','"+regiment_timing_of_therapy+"','"+regiment_tcp_outcomes+"','"+regiment_end_points_primary+"','"+regiment_end_points_secondary+"','"+media_follow_up_local_control+"','"+media_follow_up_overall_survival+"','"+media_follow_up_quality_of_life+"','"+media_ntcp_outcomes_end_point_primary+"','"+media_ntcp_outcomes_end_point_secondy+"','"+media_ntcp_outcomes_media_follow_up+"','"+ntcp_outcomes_acute+"','"+ntcp_media_g1+"','"+ntcp_media_g2+"','"+ntcp_media_g3+"','"+ntcp_media_g4+"','"+ntcp_media_g5+"','"+treatment_techniques+"','"+planing+"','"+delivery+"','"+imaging+"','"+setup+"','"+key_conclusion+"


    #,tcp_outcomes,end_point_primary,end_point_secondary,local_control,overall_survival,quality_of_life,ntcp_outcomes_end_point_primary,ntcp_outcomes_end_point_secondary,median_follow_up,acute,g1,g2,g3,g4,g5
    #'"+tcp_outcomes+"','"+end_point_primary+"','"+end_point_secondary+"','"+local_control+"','"+overall_survival+"','"+quality_of_life+"','"+ntcp_outcomes_end_point_primary+"','"+ntcp_outcomes_end_point_secondary+"','"+median_follow_up+"',"+acute+"','"+g1+"','"+g2+"','"+g3+"','"+g4+"','"+g5+"',
    result=useDB.insert("insert into protocols(author_name,protocol_name,publish_date,study_type,analysis_type,number_of_patients,study_institution,country_of_study,publication_unique_id,doi,age_range,weight_range_t,weight_range_n,weight_range_m,performance_status,cancerbyLocation,cancerbyType,histopathologic_type,histopathologic_tumor_grade,staging_system_version,classification,primary_tumor,regional_lymph_node,distant_metastasis,estrogen_receptor_status,progesterone_receptor_status,her2neu_status,dimension_range,volume_range,laterality,prior_treatment,treatment_intent,treatment_setting,base_dose_modality,additional_therapies,type_of_therapy,tcp_outcomes,end_point_primary,end_point_secondary,local_control,overall_survival,quality_of_life,ntcp_outcomes_end_point_primary,ntcp_outcomes_end_point_secondary,median_follow_up,acute,g1,g2,g3,g4,g5,regiment_treatment_intent,regiment_treatment_setting,base_dose_fraction,boost_dose_by_modality,regiment_additional_therapies,regiment_type_of_therapy,regiment_timing_of_therapy,regiment_tcp_outcomes,regiment_end_points_primary,regiment_end_points_secondary,media_follow_up_local_control,media_follow_up_overall_survival,media_follow_up_quality_of_life,media_ntcp_outcomes_end_point_primary,media_ntcp_outcomes_end_point_secondy,media_ntcp_outcomes_media_follow_up,ntcp_outcomes_acute,ntcp_media_g1,ntcp_media_g2,ntcp_media_g3,ntcp_media_g4,ntcp_media_g5,treatment_techniques,planing,delivery,imaging,setup,key_conclusion,createDateTime) values('"+study_name+"','"+protocol_name+"','"+publish_date+"','"+study_type+"','"+analysis_type+"','"+number_of_patients+"','"+study_institution+"','"+country_of_study+"','"+publication_unique_id+"','"+doi+"','"+age_range_data+"','"+weight_range_t_data+"','"+weight_range_n+"','"+weight_range_m_data+"','"+performance_status_data+"','"+cancer_by_location+"','"+cancer_by_type+"','"+histopathologic_type_data+"','"+histopathologic_tumor_grade+"','"+staging_system_version+"','"+classification_data+"','"+primary_tumor_data+"','"+regional_lymph_data+"','"+distant_metastasis_data+"','"+estrogen_receptor_status+"','"+progesterone_receptor_status+"','"+her2neu_status+"','"+dimension_range+"','"+volume_range+"','"+laterality+"','"+prior_treatment_data+"','"+treatment_intent+"','"+treatment_setting+"','"+base_dose_modality+"','"+additional_therapies+"','"+type_of_therapy_data+"','"+tcp_outcomes+"','"+end_point_primary+"','"+end_point_secondary+"','"+local_control+"','"+overall_survival+"','"+quality_of_life+"','"+ntcp_outcomes_end_point_primary+"','"+ntcp_outcomes_end_point_secondary+"','"+median_follow_up+"','"+acute+"','"+g1+"','"+g2+"','"+g3+"','"+g4+"','"+g5+"','"+regiment_treatment_intent+"','"+regiment_treatment_setting+"','"+base_dose_fraction+"','"+boost_dose_by_modality+"','"+regiment_additional_therapies+"','"+regiment_type_of_therapy_data+"','"+regiment_timing_of_therapy+"','"+regiment_tcp_outcomes+"','"+regiment_end_points_primary+"','"+regiment_end_points_secondary+"','"+media_follow_up_local_control+"','"+media_follow_up_overall_survival+"','"+media_follow_up_quality_of_life+"','"+media_ntcp_outcomes_end_point_primary+"','"+media_ntcp_outcomes_end_point_secondy+"','"+media_ntcp_outcomes_media_follow_up+"','"+ntcp_outcomes_acute+"','"+ntcp_media_g1+"','"+ntcp_media_g2+"','"+ntcp_media_g3+"','"+ntcp_media_g4+"','"+ntcp_media_g5+"','"+treatment_techniques_data+"','"+planing_data+"','"+delivery_data+"','"+imaging_data+"','"+setup_data+"','"+key_conclusion+"',NOW())")

    #result=useDB.insert("insert into protocols(study_name,protocol_name,publish_date,study_type,analysis_type,number_of_patients,study_institution,country_of_study,publication_unique_id,doi,age_range,weight_range_t,weight_range_n,weight_range_m,performance_status,cancerbyLocation,cancerbyType,histopathologic_type,histopathologic_tumor_grade,staging_system_version,classification,primary_tumor,regional_lymph_node,distant_metastasis,estrogen_receptor_status,progesterone_receptor_status,her2neu_status,dimension_range,volume_range,laterality,prior_treatment,treatment_intent,treatment_setting,base_dose_modality,additional_therapies,type_of_therapy,tcp_outcomes,end_point_primary,end_point_secondary,local_control,overall_survival,quality_of_life,ntcp_outcomes_end_point_primary,ntcp_outcomes_end_point_secondary,median_follow_up,acute,g1,g2,g3,g4,g5,regiment_treatment_intent,regiment_treatment_setting,base_dose_fraction,boost_dose_by_modality,regiment_additional_therapies,regiment_type_of_therapy,regiment_timing_of_therapy,regiment_tcp_outcomes,regiment_end_points_primary,regiment_end_points_secondary,media_follow_up_local_control,media_follow_up_overall_survival,media_follow_up_quality_of_life,media_ntcp_outcomes_end_point_primary,media_ntcp_outcomes_end_point_secondy,media_ntcp_outcomes_media_follow_up,ntcp_outcomes_acute,ntcp_media_g1,ntcp_media_g2,ntcp_media_g3,ntcp_media_g4,ntcp_media_g5,treatment_techniques,planing,delivery,imaging,setup,key_conclusion,createDateTime) values('"+study_name+"','"+protocol_name+"','"+publish_date+"','"+study_type+"','"+analysis_type+"','"+number_of_patients+"','"+study_institution+"','"+country_of_study+"','"+publication_unique_id+"','"+doi+"','"+age_range+"','"+weight_range_t+"','"+weight_range_n+"','"+weight_range_m+"','"+performance_status+"','"+cancer_by_location+"','"+cancer_by_type+"','"+histopathologic_type+"','"+histopathologic_tumor_grade+"','"+staging_system_version+"','"+classification+"','"+primary_tumor+"','"+regional_lymph_node+"','"+distant_metastasis+"','"+estrogen_receptor_status+"','"+progesterone_receptor_status+"','"+her2neu_status+"','"+dimension_range+"','"+volume_range+"','"+laterality+"','"+prior_treatment+"','"+treatment_intent+"','"+treatment_setting+"','"+base_dose_modality+"','"+additional_therapies+"','"+type_of_therapy+"','"+timing_of_therapy+"','"+tcp_outcomes+"','"+end_point_primary+"','"+end_point_secondary+"','"+local_control+"','"+overall_survival+"','"+quality_of_life+"','"+ntcp_outcomes_end_point_primary+"','"+ntcp_outcomes_end_point_secondary+"','"+median_follow_up+"','"+acute+"','"+g1+"','"+g2+"','"+g3+"','"+regiment_treatment_intent+"','"+regiment_treatment_setting+"','"+base_dose_fraction+"','"+boost_dose_by_modality+"','"+regiment_additional_therapies+"','"+regiment_type_of_therapy+"','"+regiment_timing_of_therapy+"','"+regiment_tcp_outcomes+"','"+regiment_end_points_primary+"','"+regiment_end_points_secondary+"','"+media_follow_up_local_control+"','"+media_follow_up_overall_survival+"','"+media_follow_up_quality_of_life+"','"+media_ntcp_outcomes_end_point_primary+"','"+media_ntcp_outcomes_end_point_secondy+"','"+media_ntcp_outcomes_media_follow_up+"','"+ntcp_outcomes_acute+"','"+ntcp_media_g1+"','"+ntcp_media_g2+"','"+ntcp_media_g3+"','"+ntcp_media_g4+"','"+ntcp_media_g5+"','"+treatment_techniques+"','"+planing+"','"+delivery+"','"+imaging+"','"+setup+"','"+key_conclusion+"',NOW())")
    
    print("part17")
    return json.dumps(result)


@protocol_blueprint.route('/protocol_load', methods=['GET', 'POST'])
def protocol_load():
    # useDB = AmanMySQL()
    # sql = "select Id,author_name,protocol_name,publish_date,study_type,analysis_type,number_of_patients,study_institution,country_of_study,publication_unique_id,doi,REPLACE(age_range,';','\n'),weight_range_t,weight_range_n,weight_range_m,performance_status,cancerbyLocation,cancerbyType,histopathologic_type,histopathologic_tumor_grade,staging_system_version,classification,primary_tumor,regional_lymph_node,distant_metastasis,estrogen_receptor_status,progesterone_receptor_status,her2neu_status,dimension_range,volume_range,laterality,prior_treatment,treatment_intent,treatment_setting,base_dose_modality,additional_therapies,type_of_therapy,tcp_outcomes,end_point_primary,end_point_secondary,local_control,overall_survival,quality_of_life,ntcp_outcomes_end_point_primary,ntcp_outcomes_end_point_secondary,median_follow_up,acute,g1,g2,g3,g4,g5,regiment_treatment_intent,regiment_treatment_setting,base_dose_fraction,boost_dose_by_modality,regiment_additional_therapies,regiment_type_of_therapy,regiment_timing_of_therapy,regiment_tcp_outcomes,regiment_end_points_primary,regiment_end_points_secondary,media_follow_up_local_control,media_follow_up_overall_survival,media_follow_up_quality_of_life,media_ntcp_outcomes_end_point_primary,media_ntcp_outcomes_end_point_secondy,media_ntcp_outcomes_media_follow_up,ntcp_outcomes_acute,ntcp_media_g1,ntcp_media_g2,ntcp_media_g3,ntcp_media_g4,ntcp_media_g5,treatment_techniques,planing,delivery,imaging,setup,key_conclusion from protocols"
    # getAll = useDB.get_all(sql)
    # print(json.dumps(getAll))
    # return json.dumps(getAll)


    useDB = AmanMySQL()
    sql = "select Id,author_name,protocol_name,publish_date,study_type,analysis_type,number_of_patients,study_institution,country_of_study,publication_unique_id,doi,age_range,weight_range_t,weight_range_n,weight_range_m,performance_status,cancerbyLocation,cancerbyType,histopathologic_type,histopathologic_tumor_grade,staging_system_version,classification,primary_tumor,regional_lymph_node,distant_metastasis,estrogen_receptor_status,progesterone_receptor_status,her2neu_status,dimension_range,volume_range,laterality,prior_treatment,treatment_intent,treatment_setting,base_dose_modality,additional_therapies,type_of_therapy,tcp_outcomes,end_point_primary,end_point_secondary,local_control,overall_survival,quality_of_life,ntcp_outcomes_end_point_primary,ntcp_outcomes_end_point_secondary,median_follow_up,acute,g1,g2,g3,g4,g5,regiment_treatment_intent,regiment_treatment_setting,base_dose_fraction,boost_dose_by_modality,regiment_additional_therapies,regiment_type_of_therapy,regiment_timing_of_therapy,regiment_tcp_outcomes,regiment_end_points_primary,regiment_end_points_secondary,media_follow_up_local_control,media_follow_up_overall_survival,media_follow_up_quality_of_life,media_ntcp_outcomes_end_point_primary,media_ntcp_outcomes_end_point_secondy,media_ntcp_outcomes_media_follow_up,ntcp_outcomes_acute,ntcp_media_g1,ntcp_media_g2,ntcp_media_g3,ntcp_media_g4,ntcp_media_g5,treatment_techniques,planing,delivery,imaging,setup,key_conclusion from protocols"

    getAll = useDB.get_all(sql)
    data=[]
    row_headers=useDB.get_all_headers("select Id,author_name,protocol_name,publish_date,study_type,analysis_type,number_of_patients,study_institution,country_of_study,publication_unique_id,doi,age_range,weight_range_t,weight_range_n,weight_range_m,performance_status,cancerbyLocation,cancerbyType,histopathologic_type,histopathologic_tumor_grade,staging_system_version,classification,primary_tumor,regional_lymph_node,distant_metastasis,estrogen_receptor_status,progesterone_receptor_status,her2neu_status,dimension_range,volume_range,laterality,prior_treatment,treatment_intent,treatment_setting,base_dose_modality,additional_therapies,type_of_therapy,tcp_outcomes,end_point_primary,end_point_secondary,local_control,overall_survival,quality_of_life,ntcp_outcomes_end_point_primary,ntcp_outcomes_end_point_secondary,median_follow_up,acute,g1,g2,g3,g4,g5,regiment_treatment_intent,regiment_treatment_setting,base_dose_fraction,boost_dose_by_modality,regiment_additional_therapies,regiment_type_of_therapy,regiment_timing_of_therapy,regiment_tcp_outcomes,regiment_end_points_primary,regiment_end_points_secondary,media_follow_up_local_control,media_follow_up_overall_survival,media_follow_up_quality_of_life,media_ntcp_outcomes_end_point_primary,media_ntcp_outcomes_end_point_secondy,media_ntcp_outcomes_media_follow_up,ntcp_outcomes_acute,ntcp_media_g1,ntcp_media_g2,ntcp_media_g3,ntcp_media_g4,ntcp_media_g5,treatment_techniques,planing,delivery,imaging,setup,key_conclusion from protocols")

    for result in getAll:
        data.append(dict(zip(row_headers,result)))
    
    json_data={"data":data}

    return json.dumps(json_data)
