import logging

import azure.functions as func
import mysql.connector
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    busID = req.params.get('busID')
    stationID = req.params.get('stationID')
    interactionDate = req.params.get('interactionDate')
    departureDate = req.params.get('departureDate')
    arrivalDate = req.params.get('arrivalDate')

    host= os.getenv('host')
    port=3306
    username='CC_4'
    password='1KwKNLcjP_132ngp_7kj4P5v775v8t5vQc-MQXXQjsQ'
    database='CC_4'

    cnx = mysql.connector.connect(user=username, password=password, host=host, database=database)

    cursor = cnx.cursor()

    # sql_str = f"INSERT INTO BusArrivals(Bus, Station, InteractionDate, ArrivalTime, DepartureTime) VALUES ({busID}, {stationID}, '{interactionDate}', '{arrivalDate}', '{departureDate}')"
    # rs=cursor.execute(sql_str)
    # cnx.commit()

    sql_str="SELECT * FROM BusArrivals"
    rs=cursor.execute(sql_str)
    rs=cursor.fetchall()

    return str(rs)


    # if busId and busStopId and timeStamps:
    #     return "BusId: " + busId + "\nBusStopId: " + busStopId + "\nTimeStamps: " + timeStamps
    # else:
    #     return "Some variables of these variables are missing: 'busId' or 'busStopId' or 'timeStamps' "



    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )
