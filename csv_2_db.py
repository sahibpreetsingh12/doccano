# import psycopg2
# import re
# import pandas as pd
# df=pd.read_csv('/home/sahib/Downloads/hull_contnt.csv')
# regex = re.compile(r'[\n\r\t]')
# try:
#     connection = psycopg2.connect(user="sahib",
#                                   password="sahibpreet12",
#                                   host="127.0.0.1",
#                                   port="5432",
#                                   database="sahib")
#     cursor = connection.cursor()
#     counter=0
#     postgres_insert_query = """ INSERT INTO input_data (ID, info) VALUES (%s,%s)"""
#     for i in range(len(df['0'])):
#         s = regex.sub(" ", str(df['0'][i])).strip(' ')

#         s=re.sub(' +', ' ', s) 
#         record_to_insert = (i, s)
#         cursor.execute(postgres_insert_query, record_to_insert)
#         counter+=1
#     connection.commit()
    
#     print (counter, "Records inserted successfully into Insert table")

# except (Exception, psycopg2.Error) as error :
#     if(connection):
#         print("Failed to push records into insert table", error)

# finally:
#     #closing database connection.
#     if(connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")



import psycopg2
import re
import pandas as pd
df=pd.read_csv('/home/sahib/Downloads/hull_chunks0.csv')
# regex = re.compile(r'[\n\r\t]')
try:
    connection = psycopg2.connect(user="sahib",
                                  password="sahibpreet12",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="sahib")
    cursor = connection.cursor()
    counter=0
    postgres_insert_query = """ INSERT INTO input_data (ID, info) VALUES (%s,%s)"""
    for i in range(len(df['0'])):
    # for i in range(200):
        s=df['0'][i]
        s = s.replace("\\","")
        record_to_insert = (i, s)
        cursor.execute(postgres_insert_query, record_to_insert)
        counter+=1
    connection.commit()
    
    print (counter, "Records inserted successfully into Insert table")

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to push records into insert table", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
