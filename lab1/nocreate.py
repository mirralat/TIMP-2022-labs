import os
import glob
import subprocess
from var import pwd, allowed
import time

masks = []

table = open("template.tbl", "r")
tables = []

for i in table:
    j = str(i)
    j = j.replace("\n", '')
    tables.append(j)

for i in tables:
    head, sep, tail = i.partition('.')
    tail = '*'
    i = head+tail
    masks.append(i)

print("MASK:", masks)
subprocess.run(f'sudo chmod 000 {pwd}/template.tbl', shell=True, check=True)
subprocess.run(f'sudo chattr +i {pwd}/template.tbl', shell=True, check=True)

while True:
	for name in masks:
			for file in glob.glob(name):
				if allowed == True:
					exit(0)
				if allowed == False:
					try:
						time.sleep(5)
						os.remove(file)
						print("Removed:", file)
					except:
						PermissionError