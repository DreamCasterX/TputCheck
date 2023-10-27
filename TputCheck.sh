
#!/usr/bin/env bash

# CREATOR: mike.lu@hp.com
# CHANGE DATE: 2023/10/27


# [Check Throughput Setup] 
# 1. Install required tools on Client and Partner Client
# 	(On RHEL):   sudo dnf install iperf3 
# 	(On Ubuntu): sudo apt install ssh iperf3 
#
# 2. Test and make sure SSH connection works properly 
#	ssh [partner client’s user name]@[partner client’s IP]    ex: ssh u@192.168.1.3
#
# 3. Run below command on Partner Client (once):
#	for port in `seq 52001 52007`; do iperf3 -s -D -p $port; done
#	(On RHEL):   sudo systemctl stop firewalld.service
#	(On Ubuntu): sudo systemctl stop ufw.service



[[ ! -f ./SUT_IP.txt ]] && read -p "Input partner client's IP: " SUT_IP && echo $SUT_IP > SUT_IP.txt || SUT_IP=`cat ./SUT_IP.txt`

for port in `seq 52001 52007`; do iperf3 -c $SUT_IP -p $port -f m -T $port & done | tee iperf3_output.txt

python3 rhcert/iperf3.py


