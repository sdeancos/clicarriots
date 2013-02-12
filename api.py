import urllib2
import json
import time
from datetime import datetime
from client import ClientBase

class Stream (ClientBase):

    def send (self, device, data, at, type = 'stream'):
        self._check(device, data, at, type)

        if type == 'stream':
            url = ClientBase.api_url + 'streams' 
        elif type == 'status':
            url = ClientBase.api_url + 'status'
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

class Device (ClientBase):

    def get (self, device):
        url = ClientBase.api_url + "devices/"
        if device:
            url = url + device + "/"
        else:
            raise ValueError('device value not valid')

        request = urllib2.Request(url, headers=self.headers)
        self.response = urllib2.urlopen(request)
        return self._response(self.response)

class Dropbox (ClientBase):

    def get (self, username, op = '', name = '', mime = ''):
        url = ClientBase.api_url + "external/dropbox/user/"
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