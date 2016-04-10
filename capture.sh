tcpdump -i wlan0 -s 65535 -w dump.pcap &
sleep 60
killall tcpdump
curl -i --form file=@dump.pcap http://13.92.137.252:8080/api/submit > snort_result.txt

