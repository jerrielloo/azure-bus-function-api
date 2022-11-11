import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    busId = req.params.get('busId')
    busStopId = req.params.get('busStopId')
    timeStamps = req.params.get('timeStamps')

    if busId and busStopId and timeStamps:
        return "BusId: " + busId + "\nBusStopId: " + busStopId + "\nTimeStamps: " + timeStamps
    else:
        return "Some variables of these variables are missing: 'busId' or 'busStopId' or 'timeStamps' "



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
