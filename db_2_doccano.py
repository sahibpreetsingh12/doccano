
# for local installation of doccano
# import psycopg2
# import re
# import pandas as pd
# from doccano_api_client import DoccanoClient

# doccano_client = DoccanoClient('http://0.0.0.0:8000','admin','password')

# try:
#    connection = psycopg2.connect(user="sahib",
#                                   password="sahibpreet12",
#                                   host="127.0.0.1",
#                                   port="5432",
#                                   database="sahib")
#    cursor = connection.cursor()
#    postgreSQL_select_Query = "select * from input_data"

#    cursor.execute(postgreSQL_select_Query)
   
#    records = cursor.fetchall() 
  

#    for row in records:
#     doccano_client.create_document(1,row[1])
# except (Exception, psycopg2.Error) as error :
#     print ("Error while fetching data from PostgreSQL", error)

# finally:
#     #closing database connection.
#     if(connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")


#for docker image of doccano
import psycopg2
import re
import pandas as pd
from doccano_api_client import DoccanoClient

doccano_client = DoccanoClient('http://15.207.89.34','admin','spinnaker')

try:
   connection = psycopg2.connect(user="sahib",
                                  password="sahibpreet12",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="sahib")
   cursor = connection.cursor()
   postgreSQL_select_Query = "select * from input_data limit 12000"

   cursor.execute(postgreSQL_select_Query)
   
   records = cursor.fetchall() 
  

   for row in records:
    doccano_client.create_document(1,row[1])
except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

