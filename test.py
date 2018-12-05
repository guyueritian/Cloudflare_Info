# #!/usr/bin/python3
# #-*- encoding:utf-8 -*-
# import os,sys
# import requests
# import json
# import re
# #import Info
# import datetime
#
# starttime = datetime.datetime.now()
#
# Workdir = "/home/script/Change_CloudFlare"
# NginxServer = "142.44.215.34"
#
# Api_Url = "https://api.cloudflare.com/client/v4"
# Auth_Email = "23267198@qq.com"
# Auth_Key = "12c29e4f8b9801115516755328c81e66a3ddf"
# Account_id = '732b4ea1bd8bb714c42b6e9ff2d7ef66'
#
# #data = {"type":"A","name":"aaa.01766.cc","content":"66.70.176.1","ttl":120,"proxied":'true'}
# #def Updata_IP(domain,ip,Second_Domain_ID,main_id):
# #    data = {
# #            "type": "A",
# #            "name": "%s" %domain,
# #            "content": "%s" %ip,
# #            "ttl": 120,
# #            "proxied": 'true',
# #    }
# #    response = requests.put(
# #        "https://api.cloudflare.com/client/v4/zones/%s/dns_records/%s"
# #        % (main_id,Second_Domain_ID), data=data,headers=Info.header)
#
#
# value = os.system("ping -c 1 %s &>/dev/null" % NginxServer)
# if value != 0:
#     print("服务器%s故障"%NginxServer)
#     #os.system("sh %s/countdomain.sh" % Workdir)
#     os.system("python3 %s/Info.py" % Workdir)
#
# domain = open('%s/tmpdir/domain.txt' % Workdir,'r',encoding='utf-8')
# #info = open('%s/tmpdir/domain_ip_SDID.txt' % Workdir,'r',encoding='utf-8')
# for line_domain in domain:
#     line_domain=line_domain.strip()
#     print(line_domain)
#     value = os.system('grep %s %s/tmpdir/domain_ip_SDID.txt &>/dev/null' %(line_domain,Workdir))
#     print(value)
#     if value == 0:
#         line_info = os.popen('grep %s %s/tmpdir/domain_ip_SDID.txt' %(line_domain,Workdir)).read().strip()
#         print(line_info)
#         ip = line_info.strip().split()[1]
#         alldomain = line_info.strip().split()[0]
#         primary_domain_ID = line_info.strip().split()[2]
#         Second_domain_ID = line_info.strip().split()[3]
#         print(alldomain + " " + ip + " " + primary_domain_ID + " " + Second_domain_ID)
#         #Updata_IP(alldomain,ip,primary_domain_ID,Second_domain_ID)
#         os.system('curl -X PUT https://api.cloudflare.com/client/v4/zones/%s/dns_records/%s -H "X-Auth-Email: %s" -H "X-Auth-Key: %s" -H "Content-Type: %s" --data \'{"type": "A", "name": "%s", "content": "%s", "ttl": 120, "proxied": true}\'% (primary_domain_ID, Second_domain_ID, Auth_Email,Auth_Key,\'application/json\',alldomain,\'58.218.67.138\'')
# #info.close()
# domain.close()
#
# endtime = datetime.datetime.now()
#
# #print((endtime - starttime).seconds)
import time
print( time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))