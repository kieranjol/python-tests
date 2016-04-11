import sys
import argparse

filename = sys.argv[-1]
    # Input, either file or firectory, that we want to process.
parser = argparse.ArgumentParser(description="test")
parser.add_argument('input')
parser.add_argument('-w', action='store_true',help='option W')
parser.add_argument('-c', action='store_true',help='option C')

args = parser.parse_args()

   
if args.w:
    print 'opt w'
if args.c:
    print 'opt c'

print filename
