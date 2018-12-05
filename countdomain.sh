#!/bin/bash
DirPath=/usr/local/nginx/conf/livevhosts
AllDomain=/home/script/Change_CloudFlare/tmpdir/domain.txt
RealServer=162.211.182.156:9011
[[ -f $AllDomain ]] && rm -f $AllDomain
for conf in `ls $DirPath/*.conf`
	do
		grep -q $RealServer $conf
		if [ $? -eq 0 ];then
			domain=`cat $conf | grep "server_name"|awk 'sub($1,"")'|sed 's/^[ \t]*//g'|sed 's/;//g'|sed 's/ /\n/g'`
			echo -e "$domain" >> $AllDomain
		fi
	done