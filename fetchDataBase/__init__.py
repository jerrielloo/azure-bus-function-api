import logging

import azure.functions as func
import mysql.connector
import json
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    host = os.environ["MYSQLCONNSTR_host"]
    username=os.environ["MYSQLCONNSTR_username"]
    password=os.environ["MYSQLCONNSTR_password"]
    database=os.environ["MYSQLCONNSTR_database"]

    try:
        cnx = mysql.connector.connect(user=username, password=password, host=host, database=database)

        cursor = cnx.cursor()

        sql_str_station="SELECT * FROM Station"
        rs_station=cursor.execute(sql_str_station)
        rs_station =cursor.fetchall()

        sql_str_route="SELECT * FROM Route"
        rs_route =cursor.execute(sql_str_route)
        rs_route =cursor.fetchall()

        if rs_route and rs_station:
            return func.HttpResponse(
                    json.dumps({"station": rs_station, "route": rs_route}),
                    status_code=200
                )
        else:
            return func.HttpResponse(
                    "Either station or route has no results",
                    status_code=404
                )

    except Exception as e:
        return func.HttpResponse(
            str(e),
            status_code=500
        )


    

