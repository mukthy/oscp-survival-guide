#!/bin/bash
#zone-transfer automation
#$domain -> domain name as an argument

if [ -z "$1" ]; then
	echo "[*] Zone-Transfer Automation"
	echo "[*] Usage	: $0 ./zone-transfer.sh <domain name>"
	exit 0
fi

#if the domain name was given, fetch the dns servers of the domain:

for nameserver in $(host -t ns $1 | cut -d " " -f4); do
	host -l $1 $nameserver | grep "has address"
done
