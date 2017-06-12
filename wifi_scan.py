import subprocess
import time
import argparse

print '\n---Scanning---\n'
while True:
   cmd = subprocess.Popen('sudo iwlist wlan0 scanning', shell=True,
                           stdout=subprocess.PIPE)
   for line in cmd.stdout:
        if 'Address' in line:
           addr = line.split()[4]
           print addr
        if 'Quality'in line:
            level = line.split()[2]
            print level.replace("level=", "")
        elif 'Not-Associated' in line:
            print 'No signal'
   time.sleep(0.2)
