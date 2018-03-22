"""Test module"""
import unittest
import urllib
import urllib.parse
import urllib.request
import os

class TestAPI(unittest.TestCase):
    def test_weather_api(self):
        test_url = "http://api.openweathermap.org/data/2.5/forecast?"
        params = {
            'id' : '2643743',
            'APPID' : os.environ['OPEN_WEATHER_KEY']
        }
        data = urllib.parse.urlencode( params )
        req = urllib.request.Request( test_url, data )

        assert isinstance(req)
        # res = urllib.request.urlopen( req )
        #
        # self.assertEqual( res.code, 200 )
