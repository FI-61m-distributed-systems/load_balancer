'''Python 2.7.3.'''

import sys
import time
import urllib
import urllib2
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

balance_set = ["http://127.0.0.1:8002", "http://127.0.0.1:8003"] #set for balancing

def main(argv):
    host = "127.0.0.1" #server IP 127.0.0.1
    port = 8002 #server port

    if len(argv)> 1:
        port = int(argv[1]) #server port

    try:
        HTTPServer((host,int(port)), MyServer).serve_forever()
    except:
        print 'main error'
        sys.exit(2)

class MyServer(BaseHTTPRequestHandler):
    count = 0
    def do_POST(self):

        print "header "
        print self.headers
        print "req "
        print self.request
        print "rf "
        length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(length)

        print post_data
        print "counter = "
        print self.count

        time.sleep(5)
        #param = urllib.urlencode(self.headers)
        req = urllib2.urlopen(balance_set[self.count], post_data)

        print "aft 0"
        self.count += 1

        # for_resending.getcode()
        # for_resending.headers['Content']
        self.send_response(200)
        print "aft 1"
        self.end_headers()
        print "aft 2"
        req.close()
        print "aft 3"
        # print("client_address = ", self.client_address)
        # print("server = ", self.server)
        # print("headers = ", self.headers)

        if self.count == len(balance_set):
            self.count = 0
        return
"""
    def do_GET(self):
        print "header "
        print self.headers
        print "req "
        print self.request
        print "rf "

        length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(length).decode('utf-8')

        print post_data
        print "counter = "
        print self.count

        # param = urllib.urlencode(self.headers)
        req = urllib2.urlopen(balance_set[self.count], self.headers)

        self.count += 1

        print req.getcode()
        print req.headers['Content']

        # for_resending.getcode()
        # for_resending.headers['Content']
        req.close()
        return
"""
if __name__ == '__main__':
    main(sys.argv)