clicarriots (version 0.2.0)
===============

[![Downloads](http://pepy.tech/badge/clicarriots)](http://pepy.tech/project/clicarriots)

The unofficial simple client for carriots platform (in progress) (python 2.x/3.x)

You can find more information about carriots in http://www.carriots.com/

This client only support part of API from Carriots.com: Stream and Device.

Forum: http://forum.carriots.com/

Blog: https://blog.carriots.com/

Author
------

Samuel de Ancos Martín (Core developer Carriots)

My Email: sdeancos@gmail.com

My Website: http://www.deancos.com


Install
=======

	$ pip install clicarriots

Usage
=====

Stream
======

Example send stream
-------------------
	from clicarriots import api
	from datetime import datetime

	client_stream = api.Stream("YOUR APIKEY")
	my_at = datetime.now()
	#my_at = 'now'
	data = {"KEY":"VALUE"}
	code, response = client_stream.send('ID_DEVELOPER_DEVICE', data, my_at, 'stream')
	print(code, response)

Example get stream
------------------
	from clicarriots import api
	from datetime import datetime

	client_stream = api.Stream("YOUR APIKEY")

	code, response = client_stream.get("ID_DEVELOPER_Stream")
	print(code, response)

Example get list streams
------------------------
	from clicarriots import api
	from datetime import datetime

	client_stream = api.Stream("YOUR APIKEY")
	
	#without params
	code, response = client_stream.list()
	
	#with params
	code, response = client_stream.list({"device": "MY ID DEVELOPER DEVICE"})
	
	print(code, response)

Dropbox
=======

Example get urls dropbox
------------------------
	from clicarriots import api

	client_dropbox = api.Dropbox("YOUR APIKEY")
	code, response = client_dropbox.get("YOUR FILE IN DROPBOX", op = "all", mime = "video") 
	print(code, response)

Device
======

Example get a device
--------------------
	from clicarriots import api

	client_device = api.Device("YOUR APIKEY")
	code, response = client_device.get("ID_DEVELOPER_DEVICE")
	print(code, response)

Example get list devices
------------------------
	from clicarriots import api

	client_device = api.Device("YOUR APIKEY")
	
	#without params
	code, response = client_device.list()
	
	#with params
	code, response = client_device.list({"name": "MY DEVICE NAME"})

	print(code, response)

Example create a device
-----------------------
	from clicarriots import api

	client_device = api.Device("YOUR APIKEY")
	data = {} # Valid json
	code, response = client_device.create(data)
	print(code, response)

Example update a device
-----------------------
	from clicarriots import api

	client_device = api.Device("YOUR APIKEY")
	data = {} # Valid json
	code, response = client_device.update("ID_DEVELOPER_DEVICE", data)
	print(code, response)

Example delete a device
-----------------------
	from clicarriots import api

	client_device = api.Device("YOUR APIKEY")
	code, response = client_device.delete("ID_DEVELOPER_DEVICE")
	print(code, response)

Example get types and sensors
-----------------------------
	from clicarriots import api

	client_device = api.Device("YOUR APIKEY")
	
	# Get Types
	code, response = client_device.get_types()
	
	# Get Sensors
	code, response = client_device.get_sensors()
	
	print(code, response)
