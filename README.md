clicarriots.py
===============

The unofficial simple client for carriots platform (in progress)

You can find more information about carriots in http://www.carriots.com/

Usage
=====

Example send stream
-------------------
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	from clicarriots import clicarriots
	from datetime import datetime

	def main():
	    client_carriots = clicarriots.Client("YOUR APIKEY")
	    my_at = datetime.utcnow()
	    data = {"KEY":"VALUE"}
	    code, response = client_carriots.send('YOUR ID DEVELOPER DEVICE', data, my_at, 'stream')
	    return code, response
	
	if __name__ == '__main__':
	    code, response = main()
	    print code, response
		
Example dropbox
---------------
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	from clicarriots import clicarriots
	from datetime import datetime
	
	def main():
	    client_carriots = clicarriots.Client("YOUR APIKEY")
	    code, response = client_carriots.dropbox("YOUR USERNAME", "all")
	    return code, response
	
	if __name__ == '__main__':
	    code, response = main()
	    print code, response
