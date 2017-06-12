import subprocess
import os,signal,re,shutil,time
import multiprocessing
import logging
import threading
import time, sys
import RPi.GPIO as GPIO
import time
import requests
import json

Tbtmon = None
Thcitool_lescan = None

Grssi = 0

def devID():
    cmd = "service iot status"
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line  in p.stdout.readline():
      print line.strip()[2]
#def CMD(cmd):
 #   p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  #  result = []
   # while True:
    #    line = p.stdout.readline()
     #   print line.strip()
      #  if line == '' and p.poll() != None:
       #     break
def status():
  stat = threading.Thread(target = devID)
  stat.start()
  stat.join()
if __name__ == "__main__":
 status()


