#!/bin/bash

# Install Google Chrome
echo "Installing Google Chrome..."
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get -y install -f
rm google-chrome-stable_current_amd64.deb

# Install chromedriver
echo "Installing chromedriver..."
CHROME_VERSION=$(google-chrome --version | awk '{print $3}' | awk -F '.' '{print $1}')
CHROMEDRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION")
wget "https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/
rm chromedriver_linux64.zip

echo "Chrome and chromedriver installation completed."
