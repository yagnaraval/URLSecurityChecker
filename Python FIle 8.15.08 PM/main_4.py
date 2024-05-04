from main import yagna
import requests
import json
import webbrowser  
user="ravalyagna"
password="ray"

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="raval"
)

for site in yagna.indicators:
                
                params={'apikey':yagna.api,'resource':yagna.indicators}
                page= requests.get(yagna.url, params=params)
                response= json.loads(page.content)
                
       
                
                if response['positives']<=0:
                    a = response['total']
                    b = response['positives']
                    mycursor = mydb.cursor()
                    sql2= "DELETE FROM ray"
                    mycursor.execute(sql2)

                    sql = "INSERT INTO ray (total, positives) VALUES (%s, %s)"
                    val = (a,b)
                    mycursor.execute(sql, val)

                    mydb.commit()
                    print("Total Number of TestCases: ", response['total'])
                    print("Total Number of Failed- TestCases: ", response['positives'])
                    with open('Safe URL.txt','w') as clean:
                        clean.write(site) and clean.write('\t NOT MALICIOUS\n')
                          
                        
                else:
                    a = response['total']
                    b = response['positives']
                    mycursor = mydb.cursor()
                    sql2= "DELETE FROM ray"
                    mycursor.execute(sql2)

                    sql = "INSERT INTO ray (total, positives) VALUES (%s, %s)"
                    val = (a,b)
                    mycursor.execute(sql, val)

                    mydb.commit()
                    print("Total Number of TestCases: ", response['total'])
                    print("Total Number of Failed- TestCases: ", response['positives'])
                    with open('UNSAFE URL.txt','w') as clean:
                        clean.write(site) and clean.write('\t  MALICIOUS\n')
                        
webbrowser.open_new("http://localhost/projects/cn/main/dist/")  

                    
                
                
                