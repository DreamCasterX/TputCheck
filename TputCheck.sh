#!/usr/bin/env bash

# CREATOR: mike.lu@hp.com
# CHANGE DATE: 2024/2/29


# [WiFi Throughput Check Setup] 
# 1. Make sure you can log in to the Partner Client via SSH 
#	ssh <partner client’s user name>@<partner client’s IP>    e.g., ssh u@192.168.1.3
#
# 2. Run below command on Partner Client (one-time effort):
#	`for port in `seq 52001 52002`; do iperf3 -s -D -p $port; done`
#	(On RHEL):   `sudo systemctl stop firewalld.service`
#	(On Ubuntu): `sudo systemctl stop ufw.service`


# RESTRICT USER ACCOUNT
[[ $EUID == 0 ]] && echo -e "⚠️ Please run as non-root user.\n" && exit


# Check Internet connection
CheckNetwork() {
	wget -q --spider www.google.com > /dev/null
	[[ $? != 0 ]] && echo -e "❌ No Internet connection! Check your network and retry.\n" && exit || :
}
CheckNetwork


# # Remote install
# [[ -f /usr/bin/apt ]] && PKG=apt || PKG=dnf
# case $PKG in
#   "apt")
#     	[[ ! -f /usr/bin/iperf3 ]] && CheckNetwork && sudo apt update && sudo apt install ssh iperf3 -y || : 
#   	;;
#   "dnf")
#   	[[ ! -f /usr/bin/iperf3 ]] && CheckNetwork && sudo dnf install iperf3 -y || :
#   	;;
# esac   
   

# Local install (RHEL only)
[[ ! -f /usr/bin/iperf3 ]] && CheckNetwork && sudo rpm -ivh ./rhcert/*.rpm || :


# Get parnter client's IP
[[ ! -f ./SUT_IP.txt ]] && read -p "Input partner client's IP: " SUT_IP && echo $SUT_IP > SUT_IP.txt || SUT_IP=`cat ./SUT_IP.txt`


# Run iperf test
for port in `seq 52001 52002`; do iperf3 -c $SUT_IP -p $port -f m -T $port & done | tee iperf3_output.txt


# Get result
python3 rhcert/iperf3.py


