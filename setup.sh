#!/bin/bash

if [ $# -eq 0 ] || [ $# -gt 1 ]
  then
    echo "No arguments passed in, script requires one argument, pass in 'help' for possible args"
    exit
fi

if [ $1 = "help" ]
    then
        echo "----- setup.sh Help -----"
        echo "Input forms:"
        echo "- [sudo] ./setup.sh help"
        echo "- [sudo] ./setup.sh all"
        echo "- [sudo] ./setup.sh <stage number>"
        echo ""
        echo "Input details:"
        echo "- help: outputs this menu again"
        echo "- all: sequentially executes all 3 stages listed below"
        echo "- <stage number>: executes just 1 of the 2 following stages:"
        echo "  - 1: Setup Raspberry Pi"
        echo "  - 2: Setup Python Virtual Environment"
        echo "----- setup.sh Help -----"
        exit
fi

if [ $1 -eq 1 ] || [ $1 = "all" ]
    then
        echo "---------- Executing stage 1 ----------"
        echo "---------- Running apt-get update... ----------"
        sudo apt-get update
        echo "---------- apt-get update done ----------"

        echo "---------- Setting up static IP... ----------"
        sudo apt-get install vim -y
        iface=`ip r | awk '{print $3}' | sed -n 2p`
        router_IP=`ip r | awk '{print $3}' | sed -n 1p`
        DNS_IP=`grep "nameserver" /etc/resolv.conf | awk '{print $2}'`
        desired_IP=`cat static_ip.txt`

        touch /etc/dhcpcd.conf
        echo "interface $iface" > /etc/dhcpcd.conf
        echo "static_routers=$router_IP" >> /etc/dhcpcd.conf
        echo "static domain_name_servers=$DNS_IP" >> /etc/dhcpcd.conf
        echo "static ip_address=$desired_IP/24" >> /etc/dhcpcd.conf

        cat /etc/dhcpcd.conf
        echo "---------- Done setting up static IP ----------"

        # disable and remove CUPS since it's useless
        sudo systemctl stop cups-browsed
        sudo systemctl disable cups-browsed
        sudo apt purge cups-browsed
        sudo systemctl stop cups
        sudo systemctl disable cups
        sudo apt purge cups

        sudo apt autoremove

        echo "---------- Stage 1 Setup Complete ----------"
fi

if [ $1 -eq 2 ] || [ $1 = "all" ]
    then
        echo "---------- Executing stage 2 ----------"
        echo "---------- Setting up Python Virtual Environment... ----------"
        cd /home/pi/Downloads/B.BOYT
        python -m venv ppvenv
        source ppvenv/bin/activate
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        echo "---------- Finished setting up Python Virtual Environment ----------"
        echo "---------- Stage 2 Setup Complete ----------"
fi

echo "Note: to free up extra memory, use raspi-config to set manually check option to boot to command line instead of desktop"
# script can then be run using `python3 main.py`