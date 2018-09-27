#!/usr/bin/env bash
echo "To boot your macOS in Recovery Mode inside in VMWare Fusion:;
echo "1. Choose Virtual Machine > Power On To Firmware";
echo "2. In the setup, choose 'Enter Setup' and press Enter";
echo "3. Choose 'Boom from File' and press Enter";
echo "4. Use cursor keys to find an entry named 'Recovery' and press Enter twice";
echo "5. Use cursor keys to find 'boot.efi' and press Enter";
echo
echo "Once the Recovery Mode has started:";
echo "1. Choose Utilities > Terminal";
echo "2. Type the following and press Enter:";
echo "csrutil disable; shutdown -r now;"
echo 
echo "Once macOS has booted, open Applications > Utilities > Terminal and run these commands";
sudo nvram boot-args="-v"; \
killall diskspaced; \
killall dynamic_pager; \
sudo defaults write com.apple.diskspaced minFreeSpace 0.5; \
sudo launchctl unload -w /System/Library/LaunchAgents/com.apple.diskspaced.plist; \
sudo pmset -a hibernatemode 0; \
sudo rm /var/vm/sleepimage; \
sudo launchctl unload -wF /System/Library/LaunchDaemons/com.apple.dynamic_pager.plist; \
sudo rm /var/vm/swapfile*; \
sudo shutdown -r now;

# sudo /Library/Application\ Support/VMware\ Tools/vmware-tools-cli disk shrinkonly /;
