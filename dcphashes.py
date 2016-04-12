import subprocess
import sys
import os

import pdb
#root = Tk()

# Create file-open dialog.
#root.update()

# File open dialog will appear. Whatever directory you choose will be stored as video_dir
filename = sys.argv[1]



#pdb.set_trace()
#ChunkList/Chunk/Path    
# Search through XML for filenames containing picture.


def get_count(variable,typee):
    
    
    variable = subprocess.check_output(['xmlstarlet', 'sel', 
                                             '-N', 'x=http://www.smpte-ra.org/schemas/429-8/2007/PKL',
                                             '-t', '-v', typee,
                                             filename ])
    return variable
count = get_count('count',"count(//x:Asset)")

print count


def get_hash(variable,typee,element):
    
    
        variable = subprocess.check_output(['xmlstarlet', 'sel', 
                                                 '-N', 'x=http://www.smpte-ra.org/schemas/429-8/2007/PKL',
                                                 '-t', '-m', typee,
                                                 '-v', element,
                                                 '-n', filename ])
        
        
        return variable
    



counter = 1    
while counter <= int(count):
    print count
    print counter
    picture_files = get_hash('picture_files',"//x:Asset" + "[" + str(counter) + "]" , "x:Hash")
    print picture_files
    counter += 1
    
counter = 1    
while counter <= int(count):
    print count
    print counter
    urn = get_hash('picture_files',"//x:Asset" + "[" + str(counter) + "]" , "x:Id")
    print urn
    counter += 1
print "hello"




'''                         
def get_path(variable,typee,element):
    variable = subprocess.check_output(['xml', 'sel', 
                                             '-N', 'x=http://www.digicine.com/PROTO-ASDCP-AM-20040311#',
                                             '-t', '-m', typee,
                                             '-v', element,
                                             '-n', filename ])
    return variable
path = get_path("path","//x:Asset[1]/x:ChunkList/x:Chunk","x:Path")
print path
'''                      
