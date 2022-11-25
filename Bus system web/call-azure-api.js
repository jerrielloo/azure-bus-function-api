function call_azure_api(busOrigin, busDestination, departureTime, busStop){
    var request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if( this.readyState == 4 && this.status == 200 ){
            var response_json = JSON.parse(this.responseText);
            console.log(response_json)
        }
    }
    const link = `https://busstationapi.azurewebsites.net/api/HttpTrigger1?busId=${busOrigin}&busStopId=${busStop}&timeStamps=${departureTime}&code=w4xDIMHedq0Zo1iawPfiGkcAHtTtnGXSZCHlf5-01dilAzFu610SrQ==`
    
    request.open("GET", link, true); 
    request.setRequestHeader('Content-Type', 'text/plain; charset=UTF-8');
    request.send();
}