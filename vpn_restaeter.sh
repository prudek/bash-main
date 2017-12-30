#!/bin/bash
# replace xxx.xxx.xxx.xxx on the following line with the IP address of the vpn server
VPNSERVER=xxx.xxx.xxx.xxx

RES=`/bin/ping -c 1 $VPNSERVER`
if [[ $RES == *"0 received"* ]]
then
/etc/init.d/openvpn restart
fi
exit 0 
