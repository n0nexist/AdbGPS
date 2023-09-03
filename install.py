print("INSTALLING ADBGPS AS A SERVICE")

import os

if os.getuid() != 0:
    print("you are not root.")
    exit(1)

os.system("mkdir /etc/adbgps")
os.system("cp adbgps.py /etc/adbgps")
os.system("chmod +x /etc/adbgps/adbgps.py")

username = os.popen("whoami").read().strip()

f = open("/etc/systemd/system/adbgps.service","w")
f.write(f"""[Unit]
Description=Adbgps daemon
After=network.target

[Service]
WorkingDirectory=/etc/adbgps
ExecStart=/etc/adbgps/adbgps.py
Restart=always
User={username}

[Install]
WantedBy=multi-user.target""")
f.close()

print("You can now run 'sudo systemctl start adbgps' to start the service.")
print("The device's location will be logged in /etc/adbgps/location.txt")