@app.function_name(name="BusStationAPI")
@app.route(route="req")

def main(req):
    user = req.params.get('user')
    return f'Hello, {user}!'