clicarriots.py
===============

The unofficial simple client for carriots platform (in progress)

You can find more information about carriots in http://www.carriots.com/ 

Forum: http://forum.carriots.com/

Blog: https://blog.carriots.com/

Author
------

Samuel de Ancos Martín - sdeancos@gmail.com (Core developer Carriots)


Install
=======

	$ sudo pip install git+https://github.com/sdeancos/clicarriots.git#egg=clicarriots

Usage
=====

Example send stream
-------------------
	from clicarriots import api
	from datetime import datetime

	client_stream = api.Stream("YOUR APIKEY")
	my_at = datetime.utcnow()
	data = {"KEY":"VALUE"}
	code, response = client_stream.send('YOUR ID DEVELOPER DEVICE', data, my_at, 'stream')

Example get urls dropbox
------------------------
	from clicarriots import api

	client_dropbox = api.Dropbox("YOUR APIKEY")
	code, response = client_dropbox.get("YOUR USERNAME", "all")
	return code, response
	
Example get device
------------------
	from clicarriots import api

	client_device = api.Device("YOUR APIKEY")
	code, response = client_device.get("YOUR USERNAME")
	return code, response
