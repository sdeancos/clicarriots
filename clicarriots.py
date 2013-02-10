import urllib2
import json
import time
from datetime import datetime

class Client (object):
    api_url_str = "http://api.carriots.com/streams"
    api_url_sta = "http://api.carriots.com/status"

    def __init__ (self, api_key = None, client_type = 'json', protocol = 'v2'):
        self.api_key = api_key
        self.client_type = client_type
        self.protocol = protocol
        self.content_type = "application/vnd.carriots.api.v2+%s" % \
                            (self.client_type)
        self.headers = {'User-Agent': 'clicarriots.py',
                        'Content-Type': self.content_type,
                        'Accept': self.content_type,
                        'Carriots.apikey': self.api_key}

    def send (self, device, data, at, type = 'stream'):
        self.__check(device, data, at, type)

        if type == 'stream':
            url = Client.api_url_str 
        elif type == 'status':
            url = Client.api_url_sta
        else:
            raise ValueError('type value not valid')
            
        at_timestamp = int(time.mktime(at.timetuple()))

        stream = {"protocol": self.protocol,
                  "device": device,
                  "at": at_timestamp,
                  "data": data}

        self.data = json.dumps(stream)
        request = urllib2.Request(url, self.data, self.headers)
        self.response = urllib2.urlopen(request)
        
        return self.response.code, self.response.read()
    
    def __check (self, device, data, at, type):
        if not isinstance(device, str):
            raise TypeError('device type not valid')
        
        if not isinstance(data, dict):
            raise TypeError('data type not valid')
        
        if not isinstance(at, datetime):
            raise TypeError('at type not valid')
        
        if not isinstance(type, str):
            raise TypeError('type type not valid')
