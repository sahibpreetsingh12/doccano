    # imports
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
    postgres_insert_query = """ INSERT INTO output_data (ID, info) VALUES (%s,%s)"""
    for i in range(documnet_iter_start,documnet_iter_start+total_doc):
       	s=doccano_client.get_document_detail(1,i)
       	doc_id=s['id']
       	doc_text=s['text'].replace("'","")
       	doc_ann=s['annotations']
       	temp={"text":doc_text,"annotations":doc_ann}
        cursor.execute("""INSERT INTO output_data (id,info) VALUES ( '{}','{}') """.format(doc_id,json.dumps((temp))))

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


#for testing puposes
# with open('/home/sahib/file.json') as f:
#     b=[line.split('\n', 1) for line in f]
#     for i in range(len(b)):
#         # print(len(b[i]))
        
#         temp=json.loads(b[i][0])
#         print((temp))
#         # print('\n')
