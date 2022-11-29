import mysql.connector

host='dockerlab.westeurope.cloudapp.azure.com'
port=3306
username='CC_4'
password='1KwKNLcjP_132ngp_7kj4P5v775v8t5vQc-MQXXQjsQ'
database='CC_4'

cnx = mysql.connector.connect(user=username, password=password, host=host, database=database)

cursor = cnx.cursor()

print("------TESING CONNECTION TO DATABASE-----")

sql_str="SELECT * FROM BusArrivals"
rs=cursor.execute(sql_str)
rs=cursor.fetchall()

# print(type(rs))
print(len(rs))