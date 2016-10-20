#!/usr/bin/env python
import sys
import os
import subprocess

video_dir = sys.argv[1]
for root, dirs, files in os.walk(video_dir):
    for filename in files:
        if filename.endswith(('.mov', '.mxf', '.avi', '.mp4', '.ogg', '.ogm', '.wmv','.mkv','.flv','.webm')):
            full_path = os.path.join(root,filename)
            cmd = ['mediainfo', '--Output=PBCore2', full_path]
            metadata = subprocess.check_output(cmd)
            sidecar = os.path.join(root,filename) + '.xml'
            print 'Creating PBCore sidecar for %s' % filename 
            with open(sidecar, 'w+') as fo:
                fo.write(metadata)