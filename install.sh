sudo apt update
sudo apt install -y git
sudo apt install -y python3-pip
sudo apt install -y screen
sudo apt install -y gunicron
git clone https://github.com/ytzml/polEngDict.git
cd polEngDict
pip3 install -r requirements.txt
gunicorn app:app -b 0.0.0.0:8080 --daemon
