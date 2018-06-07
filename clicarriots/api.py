# copyright (c) 2012-2018 by Samuel de Ancos
# http://deancos.com | sdeancos@gmail.com

from json import dumps
from time import mktime
from datetime import datetime

from clicarriots.client import ClientBase


class Utils (ClientBase):

    def get_time_zones(self):
        url = ClientBase.api_url + "time_zones/"

        code, response = self.request(url)

        response = [time_zones['tz'] for time_zones in response['result']]
        return code, response

    def get_locales(self):
        url = ClientBase.api_url + "locales/"

        code, response = self.request(url)

        response = [locales['locale'] for locales in response['result']]
        return code, response


class Stream (ClientBase):

    def get(self, stream):
        url = ClientBase.api_url + "streams/"
        if stream:
            url = url + stream + "/"
        else:
            raise ValueError('stream value not valid')

        response = self.request(url)
        return response

    def send(self, device, data, at, type='stream'):
        if not isinstance(device, str):
            raise TypeError('device type not valid')

        if not isinstance(data, dict):
            raise TypeError('data type not valid')

        if not isinstance(at, datetime) and not 'now':
            raise TypeError('at type not valid')

        if not isinstance(type, str):
            raise TypeError('type type not valid')

        if type == 'stream':
            url = ClientBase.api_url + 'streams'
        elif type == 'status':
            url = ClientBase.api_url + 'status'
        else:
            raise ValueError('type value not valid')

        if at != 'now':
            at = int(mktime(at.timetuple()))

        stream = {"protocol": self.protocol,
                  "device": device,
                  "at": at,
                  "data": data}


        data = dumps(stream)

        response = self.request(url, data=data, method="POST")
        return response

    def list(self, params=None):
        url = ClientBase.api_url + "streams/?"
        url = get_params(url, params)

        response = self.request(url)
        return response

    def delete(self, stream):
        url = ClientBase.api_url + "streams/"
        if stream:
            url = url + stream + "/"
        else:
            raise ValueError('stream value not valid')

        response = self.request(url, method="DELETE")
        return response


class Device (ClientBase):

    def new(self, data): ...

    def get(self, device):
        url = ClientBase.api_url + "devices/"
        if device:
            url = url + device + "/"
        else:
            raise ValueError('device value not valid')

        response = self.request(url)
        return response

    def list(self, params = None):
        url = ClientBase.api_url + "devices/?"
        url = get_params(url, params)

        response = self.request(url)
        return response

    def create(self, data):
        url = ClientBase.api_url + "devices/"

        # todo: validate data

        response = self.request(url, data=data, method="POST")
        return response

    def update(self, device, data):
        url = ClientBase.api_url + "devices/"
        if device:
            url = url + device + "/"
        else:
            raise ValueError('device value not valid')

        # todo: validate data

        response = self.request(url, data=data, method="PUT")
        return response

    def delete(self, device):
        url = ClientBase.api_url + "devices/"
        if device:
            url = url + device + "/"
        else:
            raise ValueError('device value not valid')

        response = self.request(url, method="DELETE")
        return response

    def get_types(self):
        url = ClientBase.api_url + "types/"

        code, response = self.request(url)

        response = [_type['type'] for _type in response['result']]
        return code, response

    def get_sensors(self):
        url = ClientBase.api_url + "sensors/"

        code, response = self.request(url)

        response = [sensor['sensor'] for sensor in response['result']]
        return code, response


class DeviceConfig (ClientBase):
    def create(self, device, data):
        url = ClientBase.api_url + "devices/"
        if device:
            url = url + device + "/deviceconfigs/"
        else:
            raise ValueError('device value not valid')

        response = self.request(url, data=data, method="POST")
        return response


class Dropbox (ClientBase):

    def get(self, username, op='', name='', mime=''):
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


def get_params(url, params):
    if params:
        if not isinstance(params, dict):
            raise TypeError('data type not valid')

        for key, value in params.items():
            url = url + key + "=" + value + "&"
        url = url[:-1]

    return url
