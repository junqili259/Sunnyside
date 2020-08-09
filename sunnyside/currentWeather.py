import requests


class CurrentWeather:
    def __init__(self, api_key,):
        self.api_key = api_key

    def get_current_weather_by_city_name(self, city_name):
        """
        Returns with a list of weather parameters by city name
        """
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={self.api_key}"
        response = requests.get(url=api_url)
        return response.json()

    def get_current_weather_by_city_id(self, city_id):
        """
        Returns with a list of weather parameters by city id
        Args:
            city_id: Int
        """
        api_url = f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={self.api_key}"
        response = requests.get(url=api_url)
        return response.json()
    
    def get_current_weather_by_geographic_coord(self, lat, lon):
        """
        Returns with a list of weather parameters by geo coord
        Args:
            lat: Int
            lon: Int
        """
        api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}"
        response = requests.get(url=api_url)
        return response.json()

    def get_current_weather_by_zip_code(self, zip_code, country_code="us"):
        """
        Returns with a list of weather parameters by zip code
        Args:
            zip_code: Int
            country_code: Optional
        """ 
        api_url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={self.api_key}"
        response = requests.get(url=api_url)
        return response.json()