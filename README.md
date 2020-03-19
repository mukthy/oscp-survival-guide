# OSCP-Tools/Exploits & Survival Guide

-   Set the Target IP Address to the `$ip` system variable  
    `export ip=192.168.1.100`

-   Find the location of a file  
    `locate sbd.exe`

-   Search through directories in the `$PATH` environment variable  
    `which sbd`

-   Find a search for a file that contains a specific string in it’s
    name:  
    `find / -name sbd\*`

-   Show active internet connections  
    `netstat -lntp`

-   Change Password  
    `passwd`

-   Verify a service is running and listening  
    `netstat -antp |grep apache`

-   Start a service  
    `systemctl start ssh  `
    
    `systemctl start apache2`

-   Have a service start at boot  
    `systemctl enable ssh`

-   Stop a service  
    `systemctl stop ssh`

-   Unzip a gz file  
    `gunzip access.log.gz`

-   Unzip a tar.gz file  
    `tar -xzvf file.tar.gz`

-   Search command history  
    `history | grep phrase_to_search_for`

-   Download a webpage  
    `wget http://www.cisco.com`

-   Open a webpage  
    `curl http://www.cisco.com`

-   String manipulation

    -   Count number of lines in file  
        `wc -l index.html`

    -   Get the start or end of a file  
        `head index.html`
        
        `tail index.html`

    -   Extract all the lines that contain a string  
        `grep "href=" index.html`

    -   Cut a string by a delimiter, filter results then sort  
        `grep "href=" index.html | cut -d "/" -f 3 | grep "\\." | cut -d '"' -f 1 | sort -u`

        `grep -o '[A-Za-z0-9_\.-]*\.\*cisco.com' index.html | sort -u)`

    -   Using Grep and regular expressions and output to a file  
        `cat index.html | grep -o 'http://\[^"\]\*' | cut -d "/" -f 3 | sort –u > list.txt`

    -   Use a bash loop to find the IP address behind each host  
        `for url in $(cat list.txt); do host $url; done | grep "has address" cut -d " " -f 4 | sort -u` 

    -   Collect all the IP Addresses from a log file and sort by
        frequency  
        `cat access.log | cut -d " " -f 1 | sort | uniq -c | sort -urn`

-   Netcat Banner Grabbing

    `nc -nv [IP_Address]`

-   Netcat File Transfer's

    -   Incoming Connection End

        `nc -nv [IP_Address] [PORT] > filename`

    -   Outgoing Connection End

        `nc -nv [IP_Address] [PORT] < filename`

-   TCPDUMP Commands
    
    -   To capture the traffic

        `tcpdump -r packetcap.pcap`

    -   To filter out the IP address and Port in the pcap.

        `tcpdump -n -r password_cracking_filtered.pcap | awk -F" " '{print $3}' | sort -u | head`

    -   To filter out the destination , source IP address and filter out based on Ports.

        `tcpdump -n src host 172.16.40.10 -r password_cracking_filtered.pcap`

        `tcpdump -n dst host 172.16.40.10 -r password_cracking_filtered.pcap`

        `tcpdump -n port 81 -r password_cracking_filtered.pcap`
    
    -   To use the -X flag to glean additional information from the data that was transferred.

        `tcpdump -nX -r password_cracking_filtered.pcap`

    -   Advanced Header Filtering which can show packets which should have the ACK and PSH flag set.

        `tcpdump -A -n 'tcp[13] = 24' -r password_cracking_filtered.pcap`

-   Google Hacking

    `site:"microsoft.com" -site:"www.microsoft.com"`

    `intitle:"VNC Viewer for JAVA"`

    `inurl:"/control/userimage.html"`

-   DNS Enumeration

    `host -t [type] [domain]`

    `host -t ns megacorpone.com`

    -   Simple Bash script to bruteforce the subdomain name using the host command. The list.txt contains the subdomain keywords.

        `for ip in $(cat list.txt);do host $ip.megacorpone.com; done`

    -   For performing a reverse lookup if the PTR record is maintained in the DNS Server.

        `for ip in $(seq 155 190); do host 50.7.67.$ip; done | grep -v "not found"`

    -   Zone Transfer

        `for server in $(host -t ns megacorpone.com | cut -d " " -f4); do host -l megacorpone.com $server; done`

    - 	An automation script is present in the tools.

    -	DNSRecon zone transfer

        `dnsrecon -d megacorpone.com -t axfr`

-   Port Scanning

	-	Nmap Scan ICMP 

		`nmap -v -sn 10.10.10.123 -oG ping-sweep.txt`

		`grep Up ping-sweep.txt | cut -d " " -f2`

	-	Nmap scan for top 20 ports

		`nmap -sT -A --top-ports=20 10.11.1.1-254 -oG top-port-sweep.txt`

	-	Nmap Usual scan

		`nmap -p- -sC -sV -oA nmap/initial 10.11.1.251`

	-	Nmap OS discovery

		`nmap -O 10.11.1.251`

	-	Nmap Banner Grabbing and Service Enumeration

		`nmap -sV -sT 10.11.1.251`

		`nmap -A 10.11.1.251`

	-	Nmap NSE Scripts

		`/usr/share/nmap/scripts`

		`nmap --script smb-vuln* 10.11.1.251`

	-  	For mass scanning with the list of IP's in a list we can use the below parameter -iL to mention the list and perform scanning.

		`nmap -iL ips.txt -p 80 -sV -oG web-server-version.txt`

    -   For mass scanning with the nmap using NSE script

        `nmap -iL ../lab-excercies/ips.txt --script smb-os-discovery.nse`