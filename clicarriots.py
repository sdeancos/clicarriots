import urllib2
import json
import time
from datetime import datetime
from client import ClientBase

class Client (ClientBase):
    api_url = "http://api.carriots.com/"

    def send (self, device, data, at, type = 'stream'):
        self._check(device, data, at, type)

        if type == 'stream':
            url = Client.api_url + 'streams' 
        elif type == 'status':
            url = Client.api_url + 'status'
        else:
            raise ValueError('type value not valid')
            
        at_timestamp = int(time.mktime(at.timetuple()))

        stream = {"protocol": self.protocol,
                  "device": device,
                  "at": at_timestamp,
                  "data": data}

        self.data = json.dumps(stream)
        request = urllib2.Request(url, self.data, self.headers)
        response = urllib2.urlopen(request)
        
        return self._response(response)
    
    def dropbox (self, username, op = '', name = '', mime = ''):
        url = Client.api_url + "external/dropbox/user/"
        if username:
            url = url + username
        else:
            raise ValueError('username value not valid')
        
        if op:
            url = url + "/?op=" + op
        else:
            raise ValueError('op value not valid')
        
        if op == 'file': 
            if name:
                url = url + "&name=" + name
            else:
                raise ValueError('name value not valid')
        
        if mime:
            url = url + "&mime=" + mime

        request = urllib2.Request(url, headers=self.headers)

        self.response = urllib2.urlopen(request)

        return self._response(self.response)
