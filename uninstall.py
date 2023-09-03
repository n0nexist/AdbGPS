print("UNINSTALLING ADBGPS SERVICE")

import os

if os.getuid() != 0:
    print("you are not root.")
    exit(1)

os.system("rm -r /etc/adbgps")
os.system("rm /etc/systemd/system/adbgps.service")

print("Adbgps was uninstalled")