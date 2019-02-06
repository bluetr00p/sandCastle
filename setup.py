import os
import requests
LDID_PATH = os.path.realpath('/usr/local/bin/ldid2')
os.system('chmod +x patcher')
os.system('brew install dpkg')
os.system('pip3 install pygame')
os.system('pip3 install pexpect')
#check if directory structure is in place
#check if directory structure is in place
if not os.path.exists('./patcher'):
    print('Please download/copy the rootlessJB patcher to this directory')
    sys.exit()
if not os.path.exists('./DEBS'):
    os.system('mkdir DEBS')
if not os.path.exists('./SYNC'):
    os.system('mkdir SYNC')
LDID_PATH = os.path.realpath('/usr/local/bin/ldid2')
if os.path.exists(LDID_PATH) == True:
    st = os.stat(LDID_PATH)
    oct_perm = oct(st.st_mode)
    if oct_perm[-3:] == 755:
        print(f'skipping permissions ldid2 set with: {oct_perm[-3:]}')
    else:
        print(f'ldid2 set with permissions: {oct_perm[-3:]}.\nshould be 755...')
        print('setting ldid2 permissions to 755...')
        os.chmod(LDID_PATH, 0o755)
        print('set permissions for ldid2...')
elif os.path.exists(LDID_PATH) == False:
    print('ldid2 not found...')
    try:
        print('downloading ldid2')
        r = requests.get(LDID_LINK).content
        print(r)
        print('downloaded ldid2')
        print('installing ldid2')
        open(LDID_PATH, 'wb').write(r)
        print('giving ldid2 permissions')
        os.chmod(LDID_PATH, 0o755)
        print('finished installing ldid2')
    except Exception as e:
        print(f'Error: {e}')