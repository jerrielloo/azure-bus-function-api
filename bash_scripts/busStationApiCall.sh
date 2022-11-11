#!/bin/bash
#
# This is some comment
# Here you can put how to use the script

echo -e "start of BusStationAPI call \n"

curl -X GET "https://busstationapi.azurewebsites.net/api/HttpTrigger1?busId=Sol&busStopId=2&timeStamps=2022-11-11T17:21:05.107Z&code=w4xDIMHedq0Zo1iawPfiGkcAHtTtnGXSZCHlf5-01dilAzFu610SrQ=="

echo -e "\n\n end of BusStationAPI call "

exit 0

