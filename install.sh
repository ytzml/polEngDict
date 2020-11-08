sudo apt update
sudo apt install -y git
sudo apt install -y python3-pip
sudo apt install -y screen
git clone https://github.com/ytzml/polEngDict.git
screen -S polEngDictDeploy
cd polEngDict
pip3 install -r requirements.txt
python3 app.py