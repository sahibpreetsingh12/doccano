# imports

# this script only saves those annotations which are annoatated and saves those which were not saved in final output file 

# so this script can be used for final output file
import json
import os
import psycopg2
import pandas as pd
from doccano_api_client import DoccanoClient


#client for receiving API DATA
doccano_client = DoccanoClient('http://15.207.89.34','admin','spinnaker')


total_doc=doccano_client.get_project_statistics(1)['total'] # 1 is for project_id
remaining_doc=doccano_client.get_project_statistics(1)['remaining'] # 1 is for project_id


documnet_iter_start=doccano_client.get_document_list(1)['results'][0]['id']
try:
    connection = psycopg2.connect(user="sahib",
                                  password="sahibpreet12",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="sahib")
    cursor = connection.cursor()
    
    for i in range(documnet_iter_start,documnet_iter_start+total_doc):
        s=doccano_client.get_document_detail(1,i)
        doc_id=s['id']
        doc_text=s['text'].replace("'","")
        doc_ann=s['annotations']
        temp={"text":doc_text,"annotations":doc_ann}

        if len(doc_ann)!=0: # check if list of annoatations is empty
                            # It means if list of annoatations is empty then that doc is not annoatated
         
         # select only that records that were not part of DB initially
          cursor.execute("""INSERT into output_data (id,info) select {0},'{1}' where not exists (select 1 from output_data where id={2} order by id)""".format(doc_id,json.dumps(temp),doc_id))
          
    connection.commit()
    

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to push records into insert table", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


