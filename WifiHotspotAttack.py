import subprocess

subprocess.run(['sudo', 'hostapd', 'hotspot.conf'])
arp_scan_output = subprocess.check_output(['sudo', 'arp-scan', '--localnet'])
nmap_output = subprocess.check_output(['sudo', 'nmap', '-sn', '192.168.1.0/24'])
