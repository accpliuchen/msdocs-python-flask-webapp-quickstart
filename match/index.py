from flask import Blueprint, render_template
from flask import Flask
from flask import request
from flask import session

from flask.views import View

import base64
import json
import util

from util.dbutil import AmanMySQL

match_blueprint = Blueprint('match', __name__)


@match_blueprint.route("/matchIndex")
def index():
    return "match index"


@match_blueprint.route('/match', methods=['GET', 'POST'])
def match():
   
    id =  request.form['match_patient']

    age_range =  request.form['age_range']
    weight_range =  request.form['weight_range']
    gender =  request.form['gender']
    race =  request.form['race']
    performance_status =  request.form['performance_status']

    cancer_by_location =  request.form['cancer_by_location']
    cancer_by_type =  request.form['cancer_by_type']
    histopathologic_type =  request.form['histopathologic_type']
    histopathologic_tumor_grade =  request.form['histopathologic_tumor_grade']

    staging_system_version =  request.form['staging_system_version']
    classification =  request.form['classification']

    primary_tumor =  request.form['primary_tumor']
    regional_lymph_node =  request.form['regional_lymph_node']
    distant_metastasis =  request.form['distant_metastasis']
    stage_group_clinical =  request.form['stage_group_clinical']

    pathologic_stage_primary_tumor =  request.form['pathologic_stage_primary_tumor']
    pathologic_stage_regional_lymph_node =  request.form['pathologic_stage_regional_lymph_node']
    pathologic_stage_distant_metastasis =  request.form['pathologic_stage_distant_metastasis']
    pathologic_stage_group =  request.form['pathologic_stage_group']

    psa_range =  request.form['psa_range']
    gleason_score_grading =  request.form['gleason_score_grading']
    gleason_primary_pattern =  request.form['gleason_primary_pattern']
    gleason_secondary_pattern =  request.form['gleason_secondary_pattern']
    Indication_risk_group_nccn =  request.form['Indication_risk_group_nccn']
    estrogen_receptor_status =  request.form['estrogen_receptor_status']
    progesterone_receptor_status =  request.form['progesterone_receptor_status']
    her2neu_status =  request.form['her2neu_status']

    dimension_range =  request.form['dimension_range']
    volume_range =  request.form['volume_range']
    laterality =  request.form['laterality']
    prior_treatment =  request.form['prior_treatment']
    tumor_resected =  request.form['tumor_resected']

    useDB = AmanMySQL()

    sql = "select id,full_name,medical_record_number,dob,age_Range,weight_range_t,weight_range_g,weight_range_r,performance_status,cancer_by_location,cancer_by_type,histopathologic_type,histopathologic_tumor_grade,staging_system_version,classification,primary_tumor,regional_lymph_node,distant_metastasis,estrogen_receptor_status,progesterone_receptor_status,her2neu_status,dimension_range,volume_range,laterality,prior_treatment,treatment_intent,treatment_setting,roost_dose_modality,additional_therapies,type_of_therapy,timing_of_therapy,tcp_outcomes,end_point_primary,end_point_secondary,local_control,overall_survival,quality_of_life,ntcp_outcomes_end_point_primary,ntcp_outcomes_end_point_secondy,median_follow_up,ntcp_outcomes_acute,ntcp_outcomes_g1,ntcp_outcomes_g2,ntcp_outcomes_g3,ntcp_outcomes_g4,ntcp_outcomes_g5,modality,planing,delivery,imaging,setup from patients where id="+id+" "

    getAll = useDB.get_all(sql)

    sum=0


    for result in getAll:
        patientId=result[0]

        cancerbyLocation=result[9]
        cancerbyType=result[10]
        patient_age_range=result[4]
        weight_range_t=result[5]
        weight_range_g=result[6]
        weight_range_r=result[7]
        performance_status=result[8]
 

        histopathologicType=result[11]
        histopathologicTumor_grade=result[12]

        staging_system_version_result=result[13]
        classification_result=result[14]

        #primary_tumor,regional_lymph_node,distant_metastasis
        primary_tumor_result=result[15]
        regional_lymph_node_result=result[16]
        distant_metastasis_result=result[17]

        #estrogen_receptor_status,progesterone_receptor_status,her2neu_status

        estrogen_receptor_status_result=result[18]
        progesterone_receptor_status_result=result[19]
        her2neu_status_result=result[20]
        
        #dimension_range,volume_range,laterality,prior_treatment
        dimension_range_result=result[21]
        volume_range_result=result[22]
        laterality_result=result[23]
        prior_treatment_result=result[24]

    if cancerbyLocation==None and cancerbyType==None :
       return "not match"
    
    #Id,author_name,protocol_name,publish_date,study_type,analysis_type,number_of_patients,study_institution,country_of_study,publication_unique_id,doi,age_Range,weight_range_t,weight_range_g,weight_range_r,performance_status,cancerbyLocation,cancerbyType,histopathologic_type,histopathologic_tumor_grade,staging_system_version,classification,primary_tumor,regional_lymph_node,distant_metastasis,estrogen_receptor_status,progesterone_receptor_status,her2neu_status,dimension_range,volume_range,laterality,prior_treatment,treatment_intent,treatment_setting,base_dose_modality,additional_therapies,type_of_therapy,tcp_outcomes,end_point_primary,end_point_secondary,local_control,overall_survival,quality_of_life,ntcp_outcomes_end_point_primary,ntcp_outcomes_end_point_secondary,median_follow_up,acute,g1,g2,g3,g4,g5,regiment_treatment_intent,regiment_treatment_setting,base_dose_fraction,boost_dose_by_modality,regiment_additional_therapies,regiment_type_of_therapy,regiment_timing_of_therapy,regiment_tcp_outcomes,regiment_end_points_primary,regiment_end_points_secondary,media_follow_up_local_control,media_follow_up_overall_survival,media_follow_up_quality_of_life,media_ntcp_outcomes_end_point_primary,media_ntcp_outcomes_end_point_secondy,media_ntcp_outcomes_media_follow_up,ntcp_outcomes_acute,ntcp_media_g1,ntcp_media_g2,ntcp_media_g3,ntcp_media_g4,ntcp_media_g5,treatment_techniques,planing,delivery,imaging,setup,key_conclusion 
    sql = "select * from protocols where cancerbyLocation='"+cancerbyLocation+"' and cancerbyType='"+cancerbyType+"' "
    
 
    getAllProtocols = useDB.get_all(sql)

   
    if len(getAllProtocols) !=0:
         for result in getAllProtocols:
             protocol_age_range=result[11].split(";")
             protocol_weight_range_t=result[12].split(";")
             protocol_weight_range_n=result[13]
             protocol_weight_range_m=result[14].split(";")
             protocol_performance_status=result[15].split(";")
              
             protocol_cancer_by_location=result[16]
             protocol_cancer_by_type=result[17]
             protocol_histopathologic_type=result[18].split(";")
             protocol_histopathologic_tumor_grade=result[19] 
             
             protocol_staging_system_version=result[20] 
             protocol_classification=result[21] 


             protocol_primary_tumor=result[22]
             protocol_regional_lymph_node=result[23]
             protocol_distant_metastasis=result[24]

             protocol_estrogen_receptor_status=result[25]
             protocol_progesterone_receptor_status=result[26]
             protocol_her2neu_status=result[27]


             protocol_dimension_range=result[28]
             protocol_volume_range=result[29]
             protocol_laterality=result[30]
             protocol_prior_treatment=result[31]
             
             print(protocol_cancer_by_location)
             print(protocol_cancer_by_type)
             print(protocol_histopathologic_type)
             print(protocol_histopathologic_tumor_grade)
             print(protocol_staging_system_version)
             print(protocol_classification)

             print(protocol_primary_tumor)
             print(protocol_regional_lymph_node)
             print(protocol_distant_metastasis)

             print(protocol_estrogen_receptor_status)
             print(protocol_progesterone_receptor_status)
             print(protocol_her2neu_status)

             print(protocol_dimension_range)
             print(protocol_volume_range)
             print(protocol_laterality)
             print(protocol_prior_treatment)

             result = validate_age_range(patient_age_range,protocol_age_range)
             if result==True :
                age_range_result=age_range*1
             else:
                age_range_result=0

             result = validate_weight_range_t(weight_range_t,protocol_weight_range_t)

             if result==True :
                weight_result=weight_range*1
             else:
                weight_result=0
               
             result = validate_weight_range_m(patient_age_range,protocol_weight_range_m)
             if result==True :
                race_result=race*1
             else:
                race_result=0


             if weight_range_g==protocol_weight_range_n :
                gender_result=gender*1
             else:
                gender_result=0

             result = validate_performance_status(performance_status,protocol_performance_status)
             if result==True :
                performance_status_result=performance_status*1
             else:
                performance_status_result=0


             #cancer_by_location
             if cancerbyLocation==protocol_cancer_by_location :
                protocol_cancer_by_location_result=cancer_by_location*1
             else:
                protocol_cancer_by_location_result=0

             #cancer_by_type
             if cancerbyType==protocol_cancer_by_type :
                protocol_cancer_by_type_result=cancer_by_type*1
             else:
                protocol_cancer_by_type_result=0

             #histopathologic_type
             print(histopathologicType)
             print(protocol_histopathologic_type)

             result = validate_histopathologic_type(histopathologicType,protocol_histopathologic_type)
             print(result)

             if result==True :
                histopathologic_type_result=histopathologic_type*1
             else:
                histopathologic_type_result=0

             #histopathologic_tumor_grade

             if histopathologicTumor_grade==protocol_histopathologic_tumor_grade:
                protocol_histopathologic_tumor_grade_result=histopathologic_tumor_grade*1
             else:
                protocol_histopathologic_tumor_grade_result=0

             #staging_system_version
             if staging_system_version_result==protocol_staging_system_version:
                protocol_staging_system_version_result=staging_system_version*1
             else:
                protocol_staging_system_version_result=0

             #classification

             result = validate_classification(classification_result,protocol_classification)
             if result==True :
                protocol_classification_result=classification*1
             else:
                protocol_classification_result=0

             #print(protocol_primary_tumor)
             #print(protocol_regional_lymph_node)
             #print(protocol_distant_metastasis)


             result = validate_primary_tumor(primary_tumor_result,protocol_primary_tumor)
             if result==True :
                protocol_primary_tumor=primary_tumor*1
             else:
                protocol_primary_tumor=0

             result = validate_regional_lymph_node(regional_lymph_node_result,protocol_regional_lymph_node)
             if result==True :
                protocol_regional_lymph_node=regional_lymph_node*1
             else:
                protocol_regional_lymph_node=0


             result = validate_distant_metastasis(distant_metastasis_result,protocol_distant_metastasis)
             if result==True :
                protocol_distant_metastasis=distant_metastasis*1
             else:
                protocol_distant_metastasis=0


             #estrogen_receptor_status
             if estrogen_receptor_status_result==protocol_estrogen_receptor_status:
                protocol_estrogen_receptor_status_result=estrogen_receptor_status*1
             else:
                protocol_estrogen_receptor_status_result=0

             #progesterone_receptor_status
             if progesterone_receptor_status_result==protocol_progesterone_receptor_status:
                protocol_progesterone_receptor_status_result=progesterone_receptor_status*1
             else:
                protocol_progesterone_receptor_status_result=0

             #her2neu_status
             if her2neu_status_result==protocol_her2neu_status:
                protocol_her2neu_status_result=her2neu_status*1
             else:
                protocol_her2neu_status_result=0


             #dimension_range,volume_range,laterality,prior_treatment
             if dimension_range_result==protocol_dimension_range:
                protocol_dimension_range_result=dimension_range*1
             else:
                protocol_dimension_range_result=0

             #volume_range
             if volume_range_result==protocol_progesterone_receptor_status:
                protocol_volume_range_result=volume_range*1
             else:
                protocol_volume_range_result=0

             #laterality
             if laterality_result==protocol_her2neu_status:
                protocol_laterality_result=laterality*1
             else:
                protocol_laterality_result=0   

             #prior_treatment
             if prior_treatment_result==protocol_her2neu_status:
                protocol_prior_treatment_result=prior_treatment*1
             else:
                protocol_prior_treatment_result=0   

             print('caculating........')   
             print(age_range_result)
             print(weight_result)
             print(race_result) 
             print(gender_result)
             print(performance_status_result)
             print(protocol_cancer_by_location_result) 
             print(protocol_cancer_by_type_result) 
             print(histopathologic_type_result) 
             print(protocol_histopathologic_tumor_grade_result) 
             print(protocol_staging_system_version_result) 
             print(protocol_classification_result) 

             print(protocol_primary_tumor) 
             print(protocol_regional_lymph_node) 
             print(protocol_distant_metastasis) 

             print(protocol_estrogen_receptor_status_result) 
             print(protocol_progesterone_receptor_status_result) 
             print(protocol_her2neu_status_result)

             print(protocol_dimension_range_result) 
             print(protocol_volume_range_result) 
             print(protocol_laterality_result)
             print(protocol_prior_treatment_result) 
    
             sum=int(age_range_result)+int(weight_result)+int(race_result)+int(gender_result)+int(performance_status_result)+int(protocol_cancer_by_location_result)+int(protocol_cancer_by_type_result)+int(histopathologic_type_result)+int(protocol_histopathologic_tumor_grade_result)+int(protocol_staging_system_version_result)+int(protocol_classification_result)+int(protocol_primary_tumor)+int(protocol_regional_lymph_node)+int(protocol_distant_metastasis)+int(protocol_estrogen_receptor_status_result)+int(protocol_progesterone_receptor_status_result)+int(protocol_her2neu_status_result)+int(protocol_dimension_range_result)+int(protocol_volume_range_result)+int(protocol_laterality_result)+int(protocol_prior_treatment_result)
             print('sum value'+ str(sum))
        

             result=useDB.insert("insert into matchs(age_range,weight_range,gender,race,performance_status,cancer_by_location,cancer_by_type,histopathologic_type,histopathologic_tumor_grade,staging_system_version,classification,primary_tumor,regional_lymph_node,distant_metastasis,estrogen_receptor_status,progesterone_receptor_status,her2neu_status,dimension_range,volume_range,laterality,prior_treatment,sumup,UserName,patientId,createDateTime) values('"+str(age_range_result)+"','"+str(weight_result)+"','"+str(gender_result)+"','"+str(race_result)+"','"+str(performance_status_result)+"','"+str(protocol_cancer_by_location_result)+"','"+str(protocol_cancer_by_type_result)+"','"+str(histopathologic_type_result)+"','"+str(protocol_histopathologic_tumor_grade_result)+"','"+str(protocol_staging_system_version_result)+"','"+str(protocol_classification_result)+"','"+str(protocol_primary_tumor)+"','"+str(protocol_regional_lymph_node)+"','"+str(protocol_distant_metastasis)+"','"+str(protocol_estrogen_receptor_status_result)+"','"+str(protocol_progesterone_receptor_status_result)+"','"+str(protocol_her2neu_status_result)+"','"+str(protocol_dimension_range_result)+"','"+str(protocol_volume_range_result)+"','"+str(protocol_laterality_result)+"','"+str(protocol_prior_treatment_result)+"','"+str(sum)+"','ss','"+str(patientId)+"',NOW());")

             print('insert')

             result=sum
    else:
        print("not match")
        result="not match"

    return json.dumps(result)

def validate_age_range(patients_age,protocol_age):
    
       for age in protocol_age:
            if age !="":
                if age == patients_age :
                 return True
       return False

def validate_weight_range_t(weight_range_t,protocol_weight_range_t):
    
       for range_t in protocol_weight_range_t:
            if range_t !="":
                if range_t == weight_range_t:
                 return True
       return False

def validate_weight_range_m(weight_range_m,protocol_weight_range_m):
    
       for range_m in protocol_weight_range_m:
            if range_m !="":
                if range_m == weight_range_m :
                 return True
       return False

def validate_performance_status(performance_status,protocol_performance_status):
    
       for performances in protocol_performance_status:
            if performances !="":
                if performance_status == performances :
                 return True
       return False

def validate_histopathologic_type(histopathologic_type,protocol_histopathologic_types):
    
       for histopathologic_types in protocol_histopathologic_types:
            if histopathologic_types !="":
                if histopathologic_type == histopathologic_types :
                 return True
       return False

def validate_classification(classification,protocol_classification):
    
       for classifications in protocol_classification:
            if classifications !="":
                if classification == classifications :
                 return True
       return False

def validate_primary_tumor(primary_tumor,protocol_primary_tumor):
    
       for primary_tumors in protocol_primary_tumor:
            if primary_tumors !="":
                if primary_tumor == primary_tumors :
                 return True
       return False

def validate_regional_lymph_node(regional_lymph_node,protocol_regional_lymph_node):
    
       for regional_lymph_nodes in protocol_regional_lymph_node:
            if regional_lymph_nodes !="":
                if regional_lymph_node == regional_lymph_nodes :
                 return True
       return False

def validate_distant_metastasis(distant_metastasis,protocol_distant_metastasis):
    
       for distant_metastasis in protocol_distant_metastasis:
            if distant_metastasis !="":
                if distant_metastasis == distant_metastasis :
                 return True
       return False
