import urllib2
from datetime import datetime
class ClientBase (object):
    api_url = "http://api.carriots.com/"

    def __init__ (self, api_key = None, client_type = 'json', protocol = 'v1'):
        self.api_key = api_key
        self.client_type = client_type
        self.protocol = protocol
        self.content_type = "application/vnd.carriots.api.v2+%s" % \
                            (self.client_type)
        self.headers = {'User-Agent': 'clicarriots.py',
                        'Content-Type': self.content_type,
                        'Accept': self.content_type,
                        'Carriots.apikey': self.api_key}
    
    def request(self, url, body = ''):
        if body:
            request = urllib2.Request(url, self.data, self.headers)
        else:
            request = urllib2.Request(url, headers=self.headers)
            
        response = urllib2.urlopen(request)
        return response.code, response.read()
