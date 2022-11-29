#!/bin/bash
#
# This is some comment
# Here you can put how to use the script


curl -X GET "https://busstationapi.azurewebsites.net/api/HttpTrigger1?busID=32&stationID=23&interactionDate=2008-11-11%2013:23:44&departureDate=2008-11-11%2013:23:44&arrivalDate=2008-11-11%2013:23:44&code=w4xDIMHedq0Zo1iawPfiGkcAHtTtnGXSZCHlf5-01dilAzFu610SrQ=="

datenow=$(date +'%Y-%m-%dT%H:%M:%S%z')
echo $datenow
exit 0

