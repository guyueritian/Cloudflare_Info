#!/usr/bin/python3
#-*- encoding:utf-8 -*-
import os,sys
import datetime
import configparser

ConfPath = "confdir/work.conf"
starttime = datetime.datetime.now()

Workdir = "/home/script/Change_CloudFlare"

if not os.path.exists(ConfPath):
    sys.exit("%s Not Found!" % ConfPath)

cf = configparser.ConfigParser()
cf.read(ConfPath)

Auth_Email = cf.get('CloudFlare','Auth_Email')
Auth_Key = cf.get('CloudFlare','Auth_Key')
PeerIP = cf.get('Server','PeerIP')
LocalIP = cf.get('Server','LocalIP')

#Api_Url = "https://api.cloudflare.com/client/v4"
#Auth_Email = "23267198@qq.com"
#Auth_Key = "12c29e4f8b9801115516755328c81e66a3ddf"
#Account_id = '732b4ea1bd8bb714c42b6e9ff2d7ef66'


value = os.system("ping -c 1 %s &>/dev/null" % PeerIP)
if value != 0:
    print("服务器%s故障" % PeerIP)
    #os.system("sh %s/countdomain.sh" % Workdir)
    os.system("python3 %s/Info.py" % Workdir)

domain = open('%s/tmpdir/domain.txt' % Workdir,'r',encoding='utf-8')
for line_domain in domain:
    line_domain=line_domain.strip()
    print(line_domain)
    value = os.system('grep %s %s/tmpdir/domain_ip_SDID.txt &>/dev/null' %(line_domain,Workdir))
    print(value)
    if value == 0:
        line_info = os.popen('grep %s %s/tmpdir/domain_ip_SDID.txt' %(line_domain,Workdir)).read().strip()
        print(line_info)
        ip = line_info.strip().split()[1]
        alldomain = line_info.strip().split()[0]
        Second_domain_ID = line_info.strip().split()[2]
        primary_domain_ID = line_info.strip().split()[3]
        print(alldomain + " " + ip + " " + primary_domain_ID + " " + Second_domain_ID)
        os.system('curl -X PUT https://api.cloudflare.com/client/v4/zones/%s/dns_records/%s -H "X-Auth-Email: "%s"" -H "X-Auth-Key: "%s"" -H "Content-Type: "%s"" --data \'{"type": "A", "name": "%s", "content": "%s", "ttl": 120, "proxied": true}\''% (primary_domain_ID, Second_domain_ID, Auth_Email,Auth_Key,'application/json',alldomain,LocalIP))
domain.close()

endtime = datetime.datetime.now()

print((endtime - starttime).seconds)
