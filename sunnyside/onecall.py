import requests

class OneCall():
    def __init__(self, api_key, units= None, lat= None, lon= None):
        self.api_key = api_key
        self.units = units
        self.lat = lat
        self.lon = lon

    def get_weather(self):

        if self.lon == None or self.lat == None:
            return {"cod": "400", "message": "latitude or longitude missing"}

        if self.units is None:
            api_url = f"http://api.openweathermap.org/data/2.5/onecall?lat={self.lat}&lon={self.lon}&appid={self.api_key}"
        else:
            api_url = f"http://api.openweathermap.org/data/2.5/onecall?lat={self.lat}&lon={self.lon}&units={self.units}&appid={self.api_key}"

        response = requests.get(url= api_url)
        return response.json()