'''Python 2.7.3.'''

import sys
import time
import urllib
import urllib2

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

balance_set = ["http://127.0.0.1:8002", "http://127.0.0.1:8003"] #set for balancing


def main(argv):

    host = "127.0.0.1"  # server IP 127.0.0.1
    port = 8001  # server port

    if len(argv)> 1:
        port = int(argv[1]) #server port

    try:
        print "Server send from " + host + ":" + str(port)
        HTTPServer((host,int(port)), MyServer).serve_forever()
    except:
        print 'main error'
        sys.exit(2)


class MyServer(BaseHTTPRequestHandler):

    count = 0

    def do_POST(self):
        print " To " + balance_set[self.count] + " Next data:"
        print "header "
        print self.headers
        print "req "
        print self.request
        print "rf "
        length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(length)

        print post_data

        print "counter = "+str(self.count)

        time.sleep(5)
        #param = urllib.urlencode(self.headers)
        print "Point for waiting response from "+balance_set[self.count]
        req = urllib2.urlopen(balance_set[self.count], post_data)

        print "req getcode "
        print req.getcode()
        print "req info "
        print req.info()

        self.send_response(req.getcode())
        self.send_response(req.info()) # How can we test ???
        self.end_headers()
        self.count += 1

        # for_resending.getcode()
        # for_resending.headers['Content']

        req.close()

        if self.count == len(balance_set):
            self.count = 0
        return

if __name__ == '__main__':
    main(sys.argv)