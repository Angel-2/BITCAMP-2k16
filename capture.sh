tcpdump -i wlan0 -s 65535 -w dump.pcap &
sleep 60
killall tcpdump
