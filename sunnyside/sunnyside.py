from .currentWeather import CurrentWeather
from .fiveDayForecast import FiveDayForecast
from .onecall import OneCall


class Sunnyside:
    def __init__(self, api_key, units= None, lat= None, lon= None):
        self.api_key = api_key
        self.units = units
        self.lat = lat
        self.lon = lon
    
    def current_weather(self):
        return CurrentWeather(self.api_key, self.units)

    def five_day_forecast(self):
        return FiveDayForecast(self.api_key, self.units)
    
    def one_call(self):
        return OneCall(self.api_key, self.units, self.lat, self.lon)