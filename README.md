cli-carriots.py
===============

The unofficial simple client for send streams to carriots platform

You can find more information about carriots in http://www.carriots.com/

Usage
-----
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	from clicarriots import Client
	import time, datetime

	def main():
	    client_carriots = Client ("YOUR APIKEY")
	    my_at = int(time.mktime(datetime.datetime.utcnow().timetuple()))
	    data = {"protocol": "v2",
	            "device": "YOUR DEVICE",
	            "at": my_at,
	            "data": {"KEY":"VALUE"}
	            }
	    carriots_response = client_carriots.send(data, 'stream')
	    return 0
	
	if __name__ == '__main__':
	    main()