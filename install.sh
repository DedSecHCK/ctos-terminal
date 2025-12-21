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

echo "Installation complete! Run with: ./main.py"