import mysql.connector

host='dockerlab.westeurope.cloudapp.azure.com'
port=3306
username='CC_4'
password='1KwKNLcjP_132ngp_7kj4P5v775v8t5vQc-MQXXQjsQ'
database='CC_4'

cnx = mysql.connector.connect(user=username, password=password, host=host, database=database)

cursor = cnx.cursor()

print("------TESING CONNECTION TO DATABASE-----")

sql_str="SELECT * FROM Bus"
rs=cursor.execute(sql_str)
rs=cursor.fetchall()

print(rs)

sql_str="SELECT * FROM Station"
rs=cursor.execute(sql_str)
rs=cursor.fetchall()

print(rs)


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
