#!/usr/bin/env python
"""
    Blackhole Proxy
"""
import optparse, socket, thread

class ProxyConnectionHandler(object):
    def __init__(self, connection, address, timeout=60, content="none", **kwargs):
        connection.send("HTTP/1.1 200 OK\r\nContent-type: text/html\r\nContent-length: %d\r\n\r\n%s" % (len(content), content))
        connection.close()

def start_proxy(host='localhost', port=8080, content="none"):

    try:
        print "Serving blackhole proxy on %s:%d" % (host, port)
        soc = socket.socket(socket.AF_INET)
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        soc.bind((host, port))
        soc.listen(0)

        kwargs = {"content": content}

        while True:
            args = soc.accept() + (1,)
            thread.start_new_thread(ProxyConnectionHandler, args, kwargs)
    except:
        print "Shutting blackhole proxy down..."
        soc.close()
        raise
        

if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option("-t", "--template")
    (opts, args) = parser.parse_args()

    kwargs = {}

    if opts.template:
        try: kwargs["content"] = open(opts.template).read()
        except: pass

    start_proxy(**kwargs)
