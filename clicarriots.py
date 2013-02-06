import urllib2
import json

class Client (object):
    api_url_str = "http://api.carriots.com/streams"
    api_url_sta = "http://api.carriots.com/status"

    def __init__ (self, api_key = None, client_type = 'json'):
            self.client_type = client_type
            self.api_key = api_key
            self.content_type = "application/vnd.carriots.api.v2+%s" % \
                                (self.client_type)
            self.headers = {'User-Agent': 'Python-Client-Carriots',
                            'Content-Type': self.content_type,
                            'Accept': self.content_type,
                            'Carriots.apikey': self.api_key}

    def send (self, data, type = 'stream'):
            url = Client.api_url_str if type == 'stream' else Client.api_url_sta
            self.data = json.dumps(data)
            request = urllib2.Request(url, self.data, self.headers)
            self.response = urllib2.urlopen(request)
            return self.response