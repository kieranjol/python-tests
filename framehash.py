import subprocess
import sys
import os
from glob import glob
import time
import csv

def create_csv(csv_file, *args):
    f = open(csv_file, 'wb')
    try:
        writer = csv.writer(f)
        writer.writerow(*args)
    finally:
        f.close()
        
def append_csv(csv_file, *args):
    f = open(csv_file, 'ab')
    try:
        writer = csv.writer(f)
        writer.writerow(*args)
    finally:
        f.close()

dirname = sys.argv[1]
os.chdir(dirname)
csv_report_filename = os.path.basename(dirname) + 'framehash_benchmark' + time.strftime("_%Y_%m_%dT%H_%M_%S") + '.csv'
create_csv(csv_report_filename, ('FILENAME', 'ALGORITHM', 'TIME TO COMPLETE IN SECONDS', 'PERCENTAGE INCREASE FROM FRAMEMD5'))
test_files = glob('*.y4m')
algo_list = ['murmur3', 'RIPEMD128', 'RIPEMD160', 'RIPEMD256', 'RIPEMD320', 'SHA160', 'SHA224', 'SHA256' , 'SHA512/224', 'SHA512/256', 'SHA384', 'SHA512', 'CRC32',  'adler32']
for filename in test_files:
    md5_start_time = time.time()
    subprocess.call(['ffmpeg', '-y', '-v', '0', '-i', filename, '-f', 'framehash', '-hash', 'md5', filename + '_'+ 'md5' + '_' + '.txt'])
    total_md5 =  time.time() - md5_start_time
    print filename, 'md5',total_md5
    for algorithm in algo_list:
        cmd = ['ffmpeg', '-y', '-v', '0', '-i', filename, '-f', 'framehash', '-hash', algorithm, filename + '_'+ algorithm + '_' + '.txt']
        #print cmd
        start_time = time.time()
        subprocess.call(cmd)
        total_time = time.time() - start_time

        diff = total_time - total_md5 
        diff_dive  = diff / total_md5
        percent = diff_dive * float(100)

        print filename, algorithm, total_time ,percent, '%' 
        append_csv(csv_report_filename, (filename,algorithm, total_time ,str(percent) + '%')) 

