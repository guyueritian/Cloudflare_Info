import os,sys
import json
import requests
import datetime,time
import configparser

ConfPath = "confdir/work.conf"
nowtime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
#获取配置文件
if not os.path.exists(ConfPath):
    sys.exit("%s Not Found!" % ConfPath)

cf = configparser.ConfigParser()
cf.read(ConfPath)

Auth_Email = cf.get('CloudFlare','Auth_Email')
Auth_Key = cf.get('CloudFlare','Auth_Key')
PeerIP = cf.get('Server','PeerIP')
#Api_Url = "https://api.cloudflare.com/client/v4"
#Auth_Email = "23267198@qq.com"
#Auth_Key = "12c29e4f8b9801115516755328c81e66a3ddf"
#Account_id = '732b4ea1bd8bb714c42b6e9ff2d7ef66'

Primary_Domain_ID = {
    "hdtvvip.com":"14d4275021e78e5fa3af17d14a59802c" ,
    "01766.cc":"447fcee0af275b4c1bf1dc43191a1c69"	,
    "14131.cc":"9ebb8969e66c4691221e2a075b242351",
    "dianboquliebiaomeibenshifenglba.com":"4ceaa4846d64a0e619faead9f5d7a0b0",
    "dianboquliebiaoyoubenshinizaifenga.com":"765b15ebb09005c4cb4568b2b5bbe39c",
    "easyvdieo.com":"dabc2d9c2602abe4ac3531dd817b8e6c",
    "etvb.hk":"cf9c1af5697c31cdcea447cb441d3ab2",
    "etvhk.com":"bbdd82185e50c2aa9fdcf3505d233f9c",
    "evpad.hk":"887dd10614bdacefe82aecac8a5a5c12",
    "iesaytv.com":"66168a5c16bd01fd769e20a127d4a51e",
    "ievbox.com":"01028e8edefd9e7554e33378b54c0ebc",
    "ievpad.com":"fb70857aaf5f355cf56a3540377dd55f",
    "looktvb.com":"705e87eba76c1d428d839e7aa30d304d",
    "neweasyvideo.com":"1a26575d39dc94c0d4851d98fb3c1a11",
    "tvboxmovie.com":"799e2d5b044b8a3bdd3e16bc77560021",
    "wuyelive.com":"ea6b2344486faa3ff1cabe8d5a721cea",
    "ysxhk.com":"cbe0f3ff263630f212a6d2e2cea170e3",
}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
    'Content-Type': 'application/json',
    "X-Auth-Email": "%s" % Auth_Email,
    "X-Auth-Key": "%s" % Auth_Key,
}
Export_File = '/home/script/Change_CloudFlare/tmpdir/export.txt'
domain_ip_SDID = '/home/script/Change_CloudFlare/tmpdir/domain_ip_SDID.txt'
#print(len(Domain_ID))
if os.path.exists(Export_File):
    os.system('mv %s %s_%s' %(Export_File,Export_File,nowtime))

if os.path.exists(domain_ip_SDID):
    os.remove(domain_ip_SDID)


def Get_Domain_IP():
    for key in Primary_Domain_ID:
        domainID = Primary_Domain_ID[key]
        response = requests.get('https://api.cloudflare.com/client/v4/zones/%s/dns_records/export' % domainID,headers=header)
        Text = response.text
        AllShips = Text.split(";; A Records (IPv4 addresses)",2)[1].strip()
        #print(AllShips)
        with open(Export_File,'a+',encoding='utf-8') as f:
            f.write(AllShips+"\n")
        f.close()
Get_Domain_IP()

def Get_Domain_ID():
    with open(Export_File,'r',encoding='utf-8') as f:
        for line in f:
            domain = line.strip().split()[0].rstrip('.')
            ip = line.strip().split()[-1]
            Primary_Domain = domain.split('.')[-2] + '.' + domain.split('.')[-1]
            domainID = Primary_Domain_ID[Primary_Domain]
            if ip == PeerIP:
                response = requests.get('https://api.cloudflare.com/client/v4/zones/%s/dns_records?type=A&name=%s&content=%s&page=1&per_page=40&order=type&direction=desc&match=all'
                                        % (domainID,domain,ip),headers=header)
                Json_Data = json.loads(response.text)
                Second_Domain_ID = Json_Data['result'][0]['id']
                for key in Primary_Domain_ID:
                    if Primary_Domain == key:
                        main_id = Primary_Domain_ID[key]
                        with open(domain_ip_SDID,'a+',encoding='utf-8') as _f:
                            _f.write("%s\t%s\t%s\t%s\n" %(domain,ip,Second_Domain_ID,main_id))
                        _f.close()
                        #print(domain + " " + ip + " " + Second_Domain_ID + " " + main_id)
        f.close()

Get_Domain_ID()
