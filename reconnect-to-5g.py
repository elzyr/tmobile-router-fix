import subprocess
import time


def get_wifi_info():
    result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True)
    output = result.stdout
    ssid = False
    is_5g = False
    for line in output.split('\n'):
        if "Radio type" in line:
            if "802.11a" in line or "802.11ac" in line:
                is_5g = True
        if " SSID" in line:
            ssid = line.split(":")[1].strip()
    return is_5g, ssid


def reset_wifi_connection(ssid):
    subprocess.run(['netsh', 'wlan', 'disconnect'])
    time.sleep(5)
    subprocess.run(['netsh', 'wlan', 'connect', 'name={}'.format(ssid)])
    time.sleep(5)
    print("Reconnected")


while True:
    is_5g, ssid = get_wifi_info()
    if not ssid:
        print("Could not connect to wifi")
        exit(1)
    if is_5g:
        break
    print("You are not connected to 5G, resetting connection")
    reset_wifi_connection(ssid)

print("You are connected to 5G")
