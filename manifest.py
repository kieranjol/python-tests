import sys
import subprocess
import os
filename = sys.argv[1]

dirname = os.path.dirname(filename)
print dirname
os.chdir(dirname)
dingo = os.path.normpath(filename)
var = dingo.split(os.sep)
print var[-1]
subprocess.call(['md5deep', '-ler', var[-1]])
