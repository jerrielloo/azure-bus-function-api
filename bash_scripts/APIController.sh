#!/bin/bash
#
# This is some comment
# Here you can put how to use the script


echo -e "Start of BusStationApiCall\n\n"

datenow=$(date +'%Y-%m-%dT%H:%M:%S%z')

busLine1Names=("Sol" "Gran%20Via" "Tribunal" "Bilbao" "Igelsia" "Tirso%20De%20Molina")
busLine1StationId=("110" "124" "132" "139" "153" "160")
busId="32"
timeDistance=("0" "3" "2" "5" "3" "4")

counter=0
while [ "$counter" -le 5 ]
do
    datenow=$(date -d "$datenow + ${timeDistance[counter]} minutes" +'%Y-%m-%dT%H:%M:%S%z')
    sh ./busStationApiCall.sh "$busId" ${busLine1StationId[counter]} "$datenow"
    ((counter++))
    echo -e "\n"
    sleep 2
done

echo -e "\n\nEnd of BusStationApiCall"



exit 0

