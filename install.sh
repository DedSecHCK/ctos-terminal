#!/bin/bash
# Install script for CTOS Terminal on Debian/Ubuntu

echo "Installing CTOS Terminal..."

# Update system
sudo apt update

# Install Python and pip if not installed
sudo apt install -y python3 python3-pip

# Install dependencies
pip3 install -r requirements.txt

# Make executable
chmod +x main.py

# Install globally for daily use
sudo cp main.py /usr/local/bin/ctos
sudo chmod +x /usr/local/bin/ctos

echo "Installation complete!"
echo "Run CTOS as: ctos"
echo "Or from anywhere: ./main.py"