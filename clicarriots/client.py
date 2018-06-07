# copyright (c) 2012-2018 by Samuel de Ancos
# http://deancos.com | sdeancos@gmail.com

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

import json


class ClientBase (object):
    api_url = "https://api.carriots.com/"

    def __init__(self, api_key=None, client_type='json', protocol='v2'):
        self.api_key = api_key
        self.client_type = client_type
        self.protocol = protocol
        self.content_type = "application/vnd.carriots.api.v2+%s" % self.client_type
        self.headers = {'User-Agent': 'clicarriots',
                        'Content-Type': self.content_type,
                        'Accept': self.content_type,
                        'Carriots-apikey': self.api_key}

    def request(self, url, data='', method='GET'):
        if 'GET' == method:
            response = self.method_get(url)
        elif 'POST' == method:
            response = self.method_post(url, data)
        elif 'PUT' == method:
            response = self.method_put(url, data)
        elif 'DELETE' == method:
            response = self.method_delete(url)
        else:
            raise ValueError('method not valid')

        if '20' not in str(response.code):
            return response.code, response.reason

        response_json_str = response.read().decode("utf-8")
        return response.code, json.loads(response_json_str)

    def method_get(self, url):
        request = urllib2.Request(url, headers=self.headers)

        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            return e

        return response

    def method_post(self, url, data):
        request = urllib2.Request(url, data=data, headers=self.headers)

        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            return e

        return response

    def method_put(self, url, data):
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(url, data=data, headers=self.headers)

        request.get_method = lambda: 'PUT'

        try:
            response = opener.open(request)
        except urllib2.HTTPError as e:
            return e

        return response

    def method_delete(self, url):
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(url, headers=self.headers)

        request.get_method = lambda: 'DELETE'

        try:
            response = opener.open(request)
        except urllib2.HTTPError as e:
            return e

        return response
