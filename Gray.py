import subprocess
import re


def Banner():             
    print("  _______     _______      _______     _      _       _     _     _______     _______                                               ")
    print(" |  _____|   |  ___  |    |  ___  |   | \    / |     | |   | |   |  ___  |   |_______|      ")
    print(" | |         | |___| |    | |   | |    \ \  / /      | |   | |   | |   | |      | |         ")
    print(" | |         |  _  __|    | |___| |     \ \/ /       | |___| |   | |___| |      | |         ")
    print(" | |  ___    | | \ \      |       |      \  /        | |___| |   |       |      | |         ")
    print(" | | |__ |   | |  \ \     |  / \  |       | |        | |   | |   |  / \  |      | |         ")
    print(" | |____||   | |   \ \    | /   \ |       | |        | |   | |   | /   \ |      | |         ")
    print(" |_______|   |_|    \_\   |/     \|       |_|        |_|   |_|   |/     \|      |_|         ")
    print("                                     Only on Linux                                          ")
    print(f"BY: Crashi                          Version 1.0                                            ")
    print()
    print()
    print("Hotspot IP-Tracker[1]")
    print()
    print("IP-ATTACK[2]")
    print()
Banner()    
x = int(input("Enter the attack number: "))
if x == 1:
    nmap_output = subprocess.check_output(['sudo', 'nmap', '-sn', '192.168.0.0/24'])
    nmap_output = nmap_output.decode('utf-8')
    pattern = re.compile(r'Host (\d+\.\d+\.\d+\.\d+) .*?([0-9A-Fa-f:]{17}) \((.*?)\)')
    matches = pattern.findall(nmap_output)
  
    config_file_path = "hotspot.conf"
  
    for ip, mac, device_name in matches:
        filename = f"{device_name}.txt"
        with open(filename, "w") as file:
            file.write(f"IP cím: {ip}")
    subprocess.run(['sudo', 'systemctl', 'unmask', 'hostapd'])
    subprocess.run(['sudo', 'systemctl', 'start', 'hostapd'])
if x == 2:
    print("Comming soon ")
else:
    print("Fatal ERROR")    
