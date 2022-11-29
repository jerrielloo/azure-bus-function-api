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

    host = os.environ["MYSQLCONNSTR_host"]
    username=os.environ["MYSQLCONNSTR_username"]
    password=os.environ["MYSQLCONNSTR_password"]
    database=os.environ["MYSQLCONNSTR_database"]

    try:
        cnx = mysql.connector.connect(user=username, password=password, host=host, database=database)

        cursor = cnx.cursor()

        sql_str = f"INSERT INTO BusArrivals(Bus, Station, ArrivalTime, DepartureTime) VALUES ({busID}, {stationID}, '{arrivalDate}', '{departureDate}')"
        rs=cursor.execute(sql_str)
        cnx.commit()

        sql_str=f"SELECT * FROM BusArrivals WHERE Station = {stationID}"
        rs=cursor.execute(sql_str)
        rs=cursor.fetchall()

        if rs:
            return func.HttpResponse(
                "Bus ID: " + str(rs[0][0]) +"\nStation ID: " + str(rs[0][1]) + "\nArrival Time: " + str(rs[0][2]) + "\nDeparture Time: " + str(rs[0][3]),
                status_code = 200
            )
        else:
            return func.HttpResponse(
                "No result found",
                status_code = 404
            )
    except Exception as e:
        return func.HttpResponse(
            str(e),
            status_code=500
        )

