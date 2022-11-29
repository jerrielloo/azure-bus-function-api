import mysql.connector

host='dockerlab.westeurope.cloudapp.azure.com'
port=3306
username='CC_4'
password='1KwKNLcjP_132ngp_7kj4P5v775v8t5vQc-MQXXQjsQ'
database='CC_4'

cnx = mysql.connector.connect(user=username, password=password, host=host, database=database)

cursor = cnx.cursor()

print("------TESING CONNECTION TO DATABASE-----")
# sql_str = "SELECT * FROM BusArrivals;"
# rs=cursor.execute(sql_str)
# rs=cursor.fetchall()
busID = 32
stationID = 110
interactionDate = "2008-11-11 13:23:44"
departureDate = "2008-11-11 13:23:44"
arrivalDate ="2008-11-11 13:23:44"

# sql_str = f"INSERT INTO BusArrivals(Bus, Station, InteractionDate, ArrivalTime, DepartureTime) VALUES ({busID}, {stationID}, '{interactionDate}', '{arrivalDate}', '{departureDate}')"
# # sql_str = "INSERT INTO BusArrivals(Bus, Station, InteractionDate,ArrivalTime, DepartureTime) VALUES (32, 24, '2008-11-11 13:23:44', '2008-11-11 13:23:44', '2008-11-11 13:23:44')"
# rs=cursor.execute(sql_str)
# cnx.commit()

sql_str="SELECT * FROM Bus"
rs=cursor.execute(sql_str)
rs=cursor.fetchall()

print(rs)