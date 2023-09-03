# AdbGPS
Use your android phone as a gps module for your pc

# Requirements
<ul>
  <li>A linux computer</li>
  <li>An android phone with gps location enabled and Google Maps opened</li>
  <li>Adb installed on the linux computer</li>
</ul>

# Install
```
git clone https://github.com/n0nexist/AdbGPS
cd AdbGPS
sudo python3 install.py
```
<br>
the script will install the <b><u>adbgps</u></b> service. while the service is running, the device's location will be logged in /etc/adbgps/location.txt in a json format.
to uninstall the script, run the <b>uninstall.py</b> script with root privileges
