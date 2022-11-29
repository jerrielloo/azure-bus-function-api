import mysql.connector
import json

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
busID = 9
stationID = 110
# interactionDate = "2008-11-11 13:23:44"
departureDate = "2011-10-05T14:48:00.000Z"
arrivalDate ="2011-10-05T14:48:00.000Z"

sql_str = f"INSERT INTO BusArrivals(Bus, Station, ArrivalTime, DepartureTime) VALUES ({busID}, {stationID}, '{arrivalDate}', '{departureDate}')"
# # sql_str = "INSERT INTO BusArrivals(Bus, Station, InteractionDate,ArrivalTime, DepartureTime) VALUES (32, 24, '2008-11-11 13:23:44', '2008-11-11 13:23:44', '2008-11-11 13:23:44')"
rs=cursor.execute(sql_str)
cnx.commit()

# sql_str="SELECT * FROM Bus"
# rs=cursor.execute(sql_str)
# rs=cursor.fetchall()
# sql_str_station="SELECT * FROM Station"
# rs_station=cursor.execute(sql_str_station)
# rs_station =cursor.fetchall()

sql_str_route="SELECT * FROM BusArrivals"
rs_route =cursor.execute(sql_str_route)
rs_route =cursor.fetchall()


# print(json.dumps({"station": rs_station, "route": rs_route}))
# print(str({"station": rs_station, "route": rs_route}))

print(rs_route)