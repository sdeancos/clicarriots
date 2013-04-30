clicarriots.py
===============

The unofficial simple client for carriots platform (in progress)

You can find more information about carriots in http://www.carriots.com/ 

Forum: http://forum.carriots.com/

Blog: https://blog.carriots.com/

Author
------

Samuel de Ancos Martín (Core developer Carriots https://www.carriots.com/about_us)

My Email: sdeancos@gmail.com

My Website: http://www.deancos.com


Install
=======

	$ sudo pip install git+https://github.com/sdeancos/clicarriots.git#egg=clicarriots

Usage
=====

Stream
======

Example send stream
-------------------
	from clicarriots import api
	from datetime import datetime

	client_stream = api.Stream("YOUR APIKEY")
	my_at = datetime.utcnow()
	data = {"KEY":"VALUE"}
	code, response = client_stream.send('YOUR ID DEVELOPER DEVICE', data, my_at, 'stream')

Example get list streams
------------------------
	from clicarriots import api
	from datetime import datetime

	client_stream = api.Stream("YOUR APIKEY")
	
	#without params
	code, response = client_stream.list()
	
	#with params
	code, response = client_stream.list({"id_device": "MY ID DEVELOPER DEVICE"})
	
	return code, response

Dropbox
=======

Example get urls dropbox
------------------------
	from clicarriots import api

	client_dropbox = api.Dropbox("YOUR APIKEY")
	code, response = client_dropbox.get("YOUR USERNAME", op = "all", mime = "video") 
	return code, response

Device
======

Example get a device
--------------------
	from clicarriots import api

	client_device = api.Device("YOUR APIKEY")
	code, response = client_device.get("YOUR USERNAME")
	return code, response

Example get list devices
------------------------
	from clicarriots import api

	client_device = api.Device("YOUR APIKEY")
	
	#without params
	code, response = client_device.list()
	
	#with params
	code, response = client_device.list({"name": "MY DEVICE NAME"})

	return code, response
