# Sunnyside

[![GitHub release](https://img.shields.io/github/v/release/junqili259/Sunnyside.svg)](https://github.com/junqili259/Sunnyside/releases)
[![Github all releases](https://img.shields.io/github/downloads/junqili259/Sunnyside/total)](https://github.com/junqili259/Sunnyside/releases)
![Python Version](https://img.shields.io/pypi/pyversions/sunnyside)

## Installation
```
pip3 install sunnyside
```

## Getting Started
### Python Version
Sunnyside only supports python 3.6+
_________________________________________________________________________________________________________________________________________________________________________________

## Current Weather
#### Weather by city name
```python
import sunnyside

ref = sunnyside.CurrentWeather("YOUR-API-KEY-HERE")
response = ref.get_current_weather_by_city_name("Brooklyn")
```
#### Weather by city id
```python
ref.get_current_weather_by_city_id("city_id")
```
#### Weather by coordinates 
```python
ref.get_current_weather_by_geographic_coord("lat","lon")
```
#### Weather by zip code
```python
ref.get_current_weather_by_zip_code("zipcode")
```

_________________________________________________________________________________________________________________________________________________________________________________

