#!/bin/bash
#
# This is some comment
# Here you can put how to use the script


echo -e "Start of BusStationApiCall\n\n"

datenow=$(date +'%Y-%m-%d %H:%M:%S')
DATE=$(echo "$datenow" | cut -b-10)
TIME=$(echo "$datenow" | cut -b12-)
TIMESTAMP=$(echo "$DATE%20$TIME")

busLine1Names=("Batan" "Lago" "Plaza%20De%20España" "Tribunal" "Alonso%20Martinez" "Gregorio%20Marañon")
busLine2StationId=("207" "213" "220" "132" "233" "242")
bus2Id="65"
timeDistance=("2" "2" "1" "4" "3")
# datetime="2008-11-11%2013:23:44"
counter=0
while [ "$counter" -le ${#busLine1Names[@]} ]
    do
        datenow=$(date -d "$datenow + ${timeDistance[counter]} minutes" +'%Y-%m-%dT%H:%M:%S%z')
        ARRIVAL_DATE=$(echo "$datenow" | cut -b-10)
        ARRIVAL_TIME=$(echo "$datenow" | cut -b12-)
        ARRIVAL_TIMESTAMP=$(echo "$DATE%20$TIME")

        datenow=$(date -d "$datenow + 1 minutes" +'%Y-%m-%dT%H:%M:%S%z')
        DEPARTURE_DATE=$(echo "$datenow" | cut -b-10)
        DEPARTURE_TIME=$(echo "$datenow" | cut -b12-)
        DEPARTURE_TIMESTAMP=$(echo "$DATE%20$TIME")

        sh ./busStationApiCall.sh "$bus2Id" "${busLine2StationId[counter]}" "$ARRIVAL_TIMESTAMP" "$DEPARTURE_TIMESTAMP"
        ((counter++))
        echo -e "\n"
        sleep 2
done
echo $TIMESTAMP
echo -e "\n\nEnd of BusStationApiCall"



exit 0

