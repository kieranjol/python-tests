import csv
import sys

filename = sys.argv[1]
with open(filename) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if "England" in row['Country of Origin']:
            print row
        
