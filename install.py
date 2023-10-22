config = """\
interface=wlan0
driver=nl80211
ssid=YourHotspotName
hw_mode=g
channel=6
wpa=2
wpa_passphrase=YourPassword
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
"""

with open("/home/felhasznalo/hotspot.conf", "w") as config_file:
    config_file.write(config)
