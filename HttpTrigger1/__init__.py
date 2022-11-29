import logging

import azure.functions as func
import mysql.connector
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    busID = req.params.get('busID')
    stationID = req.params.get('stationID')
    departureDate = req.params.get('departureDate')
    arrivalDate = req.params.get('arrivalDate')

    # host = 'dockerlab.westeurope.cloudapp.azure.com'
    host = os.environ["SQLCONNSTR_host"]
    port=3306
    username='CC_4'
    password='1KwKNLcjP_132ngp_7kj4P5v775v8t5vQc-MQXXQjsQ'
    database='CC_4'

    try:
        cnx = mysql.connector.connect(user=username, password=password, host=host, database=database)

        cursor = cnx.cursor()

        sql_str = f"INSERT INTO BusArrivals(Bus, Station, ArrivalTime, DepartureTime) VALUES ({busID}, {stationID}, '{arrivalDate}', '{departureDate}')"
        rs=cursor.execute(sql_str)
        cnx.commit()

        sql_str=f"SELECT * FROM BusArrivals WHERE Station = {stationID}"
        rs=cursor.execute(sql_str)
        rs=cursor.fetchall()

        return "Bus ID: " + str(rs[0][0]) +"\nStation ID: " + str(rs[0][1]) + "\nArrival Time: " + str(rs[0][2]) + "\nDeparture Time: " + str(rs[0][3])
    except Exception as e:
        return e

