
import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64
import os

def get_weather():
    params = urllib.parse.urlencode({
        'id' : '2643743',
        'APPID' : os.environ['OPEN_WEATHER_KEY'],
    })

    try:
        conn = http.client.HTTPSConnection('api.openweathermap.org')
        conn.request("GET", "/data/2.5/forecast?%s" % params)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
