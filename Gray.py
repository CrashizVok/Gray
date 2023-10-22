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
    def create_hotspot():
    subprocess.run(['sudo', 'systemctl', 'unmask', 'hostapd'])
    subprocess.run(['sudo', 'systemctl', 'start', 'hostapd'])

    def track_connected_devices():
        connected_devices = set() 
    
        while True:
            nmap_output = subprocess.check_output(['sudo', 'nmap', '-sn', '192.168.0.0/24'])
            nmap_output = nmap_output.decode('utf-8')
            pattern = re.compile(r'Host (\d+\.\d+\.\d+\.\d+) .*?([0-9A-Fa-f:]{17}) \((.*?)\)')
            matches = pattern.findall(nmap_output)
    
            for ip, mac, device_name in matches:
                if mac not in connected_devices:
                    print(f"Célpont bemérve: {device_name} ({ip})")
                    connected_devices.add(mac)
            
            disconnected_devices = connected_devices.copy()
            for ip, mac, _ in matches:
                if mac in disconnected_devices:
                    disconnected_devices.remove(mac)
            
            for mac in disconnected_devices:
                print(f"{mac} lecsatlakozott")
            time.sleep(60) 
    create_hotspot()
    track_connected_devices()
    #tenksz jú
if x == 2:
    print("Comming soon ")
else:
    print("Fatal ERROR")    
