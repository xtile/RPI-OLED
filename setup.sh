sudo wget https://raw.githubusercontent.com/DIYElectronicsZA/RPi-OLED-1.3-HAT-WaveShare/master/Python3.tar.gz
sudo tar -xzf Python3.tar.gz
cd Python3
sudo apt-get update --allow-releaseinfo-change
sudo apt-get upgrade -y
sudo apt-get install python3-dev python3-pip libffi-dev libssl-dev -y
sudo -H pip3 install --upgrade pip -y
sudo apt-get purge python3-pip -y
sudo -H pip3 install --upgrade luma.oled
sudo pip3 install smbus 
sudo apt-get install python3-numpy -y
sudo apt-get install libopenjp2-7 -y
sudo apt install libtiff5 -y

#sudo Python3 Demo