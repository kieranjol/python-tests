#http://stackoverflow.com/a/89919/2188572

import re
import sys
import os

filename = os.path.basename(sys.argv[1])
print filename

if re.match("^[A-Za-z0-9\-_\.]*$", filename):
    print "all is well"
else:
    print "illegal characters"
