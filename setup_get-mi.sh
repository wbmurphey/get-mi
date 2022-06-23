chmod +x ./get-mi.py
mkdir $HOME/scripts 2>/dev/null && mkdir $HOME/scripts/Python 2>/dev/null
cp ./get-mi.py $HOME/scripts/Python/get-mi.py
sudo rm /usr/local/bin/get-mi
sudo ln -s $HOME/scripts/Python/get-mi.py /usr/local/bin/get-mi