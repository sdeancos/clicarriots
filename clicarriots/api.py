import json
import time
from datetime import datetime
from client import ClientBase

class Stream (ClientBase):

    def send (self, device, data, at, type = 'stream'):        
        if not isinstance(device, str):
            raise TypeError('device type not valid')
        
        if not isinstance(data, dict):
            raise TypeError('data type not valid')
        
        if not isinstance(at, datetime):
            raise TypeError('at type not valid')
        
        if not isinstance(type, str):
            raise TypeError('type type not valid')

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
        
        response = self.request(url, self.data)
        return response

class Device (ClientBase):

    def get (self, device):
        url = ClientBase.api_url + "devices/"
        if device:
            url = url + device + "/"
        else:
            raise ValueError('device value not valid')

        response = self.request(url)
        return response

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

        response = self.request(url)
        return response