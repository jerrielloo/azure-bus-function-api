import logging

import azure.functions as func
import mysql.connector
import json
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    host='dockerlab.westeurope.cloudapp.azure.com'
    port=3306
    username='CC_4'
    password='1KwKNLcjP_132ngp_7kj4P5v775v8t5vQc-MQXXQjsQ'
    database='CC_4'

    try:
        cnx = mysql.connector.connect(user=username, password=password, host=host, database=database)

        cursor = cnx.cursor()

        sql_str_station="SELECT * FROM Station"
        rs_station=cursor.execute(sql_str_station)
        rs_station =cursor.fetchall()

        # sql_str_route="SELECT * FROM Route"
        # rs_route =cursor.execute(sql_str_route)
        # rs_route =cursor.fetchall()

        return rs_station

    except Exception as e:
        return e


    

