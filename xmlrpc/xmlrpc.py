import sys, os, xmlrpclib

sys.stderr = sys.stdout

MAX_REQUEST = 50000

def giveup(message):
    print "Status: 400"
    print
    print "sorry,", message
    sys.exit(0)

if os.environ.get("REQUEST_METHOD") != "POST":
    giveup("invalid request")

bytes = int(os.environ.get("CONTENT_LENGTH", 0))
if bytes > MAX_REQUEST:
    giveup("request too large")

params, method = xmlrpclib.loads(sys.stdin.read(bytes))

result = dispatch(method, params)

if not isinstance(result, type(())):
    result = (result,)

response = xmlrpclib.dumps(result, methodresponse=1)

print "Content-Type: text/xml"
print "Content-Length:", len(response)
print
print response
