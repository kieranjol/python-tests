import sys
import subprocess
import os
filename = sys.argv[1]
manifest = sys.argv[1] + 'manifest.md5'

dirname = os.path.dirname(filename)
print dirname
os.chdir(dirname)
dingo = os.path.normpath(filename)
var = dingo.split(os.sep)
print var[-1]
manimani = subprocess.check_output(['md5deep', '-ler', var[-1]])

with open(manifest,"w+") as fo:
	fo.write(manimani)
