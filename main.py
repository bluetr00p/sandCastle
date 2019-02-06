import sys
import os
import shutil
from glob import glob
import pexpect
#import pygame

##FOLDER AND FILE STRUCTURE INTEGRITY
#check if directory structure is in place
if not os.path.exists('./patcher'):
    print('Please download/copy the rootlessJB patcher to this directory')
    sys.exit()
if not os.path.exists('./DEBS'):
    os.system('mkdir DEBS')
if not os.path.exists('./SYNC'):
    os.system('mkdir SYNC')
LDID_PATH = os.path.realpath('/usr/local/bin/ldid2')
#get current working directory
cwd = os.getcwd()

print('Welcome to sandCastle!')
clientDevice = str(input('iDevice IPADDRESS: '))
clientPASS = input('iDevice ROOT Password: ')
if bool(clientPASS) == False:
    clientPASS = 'alpine'
#comple the tweaks into rootlessJB3 things
directoryDEBS = glob('DEBS/*')
i = 0
for debFile in directoryDEBS:
    deb_path = debFile
    out_path = cwd + '/SYNC'
    query = './patcher' + " " + deb_path + " " + out_path
    os.system(query)
    files = []
    pattern = '*.dylib'
    for dir,_,_ in os.walk(cwd):
        files.extend(glob(os.path.join(dir, pattern)))
    for i in range(len(files)):
        os.system(f'ldid2 -S {files[i]}')
    #remove debian folder as it is not usable currently
    shutil.rmtree('./SYNC/DEBIAN')
    i += 1
    
#sync the files over