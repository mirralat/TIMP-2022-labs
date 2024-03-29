import subprocess
from var import pwd


names = []
ls = subprocess.Popen(["ls", "-p", "."],  stdout=subprocess.PIPE,)
grep = subprocess.Popen(["grep", "-v", "/$"],  stdin=ls.stdout, stdout=subprocess.PIPE,)
files = grep.stdout

for line in files:
    line = str(line, 'utf-8')
    line = line.replace("\n", '')  
    names.append(line)

table = open("template.tbl", "r")
tables = []

for i in table:
    j = str(i)
    j = j.replace("\n", '')
    tables.append(j)


for line in tables:
	if line in names:
		subprocess.run(f'sudo chmod 000 {pwd}/{line}', shell=True, check=True)
		subprocess.run(f'sudo chattr +i {pwd}/{line}', shell=True, check=True)


