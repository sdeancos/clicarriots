from datetime import datetime
class ClientBase (object):
    api_url = "http://api.carriots.com/"

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
    
    def _response (self, response):
        return response.code, response.read()
    
    def _check (self, device, data, at, type):
        if not isinstance(device, str):
            raise TypeError('device type not valid')
        
        if not isinstance(data, dict):
            raise TypeError('data type not valid')
        
        if not isinstance(at, datetime):
            raise TypeError('at type not valid')
        
        if not isinstance(type, str):
            raise TypeError('type type not valid')
