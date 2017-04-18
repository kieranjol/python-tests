#!/usr/bin/env python
import os
import shutil
import sys


def main():
    '''''
    argv[1] = input
    argv[2] = copy destination
    argv[3] = dropbox reference
    '''
    dropbox_list = []
    for root, dirames, filenames in os.walk(sys.argv[3]):
        
        for filename in filenames:
            if '_h264' in filename:
                h264_path = os.path.join(root, filename)
                dropbox_list.append(filename)
        print dropbox_list
    input = sys.argv[1]
    for root, dirames, filenames in os.walk(sys.argv[1]):
        for filename in filenames:
            if '_h264' in filename:
                h264_path = os.path.join(root, filename)
                if filename not in dropbox_list:
                    print 'copying', filename
                    shutil.copy(h264_path,sys.argv[2])
    

if __name__ == '__main__':
    main()