#!/bin/bash


COMMANDS=("/usr/sbin/service vsftpd" "systemctl")

SUDO_ENTRIES=("ALL ALL=($USER) NOPASSWD: ${COMMANDS[0]}" "ALL ALL=($USER) NOPASSWD: ${COMMANDS[1]}")

for entry in "${SUDO_ENTRIES[@]}"; do
    echo "$entry" | sudo tee -a /etc/sudoers >/dev/null
done
echo "Done"
