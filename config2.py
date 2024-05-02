#!/usr/bin/env python3

import subprocess

# Define the commands
COMMANDS = ["/usr/sbin/service vsftpd", "systemctl"]

# Define the sudoers entries
SUDO_ENTRIES = ["ALL ALL=(ALL) NOPASSWD: " + command for command in COMMANDS]

# Add sudoers entries
for entry in SUDO_ENTRIES:
    subprocess.run(["sudo", "sh", "-c", f'echo "{entry}" >> /etc/sudoers'])

print("Sudo configurations added for all users.")
