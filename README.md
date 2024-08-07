# WiFi 5G Auto Reconnect Script

This Python script checks if your WiFi connection is on a 5GHz network and automatically resets the connection if it is not.

## Prerequisites

- Python 3.x
- Windows operating system

## How It Works

1. The script uses the `netsh` command-line utility to gather information about the current WiFi connection.
2. It checks if the WiFi connection is on a 5GHz network by looking for `802.11a` or `802.11ac` in the output.
3. If the connection is not on a 5GHz network, it disconnects and reconnects to the specified SSID.

## Usage

1. Clone this repository or download the script.
2. Ensure you have Python 3.x installed on your system.
3. Open a command prompt and navigate to the directory containing the script.
4. Run the script with `python reconnect-to-5g.py`.
