clear
cd
rm -rf $HOME/BlackBIN
figlet "ATUALIZANDO" | lolcat
figlet "AGUARDE..." | lolcat
figlet "ABRINDO GIT HUB" | lolcat
am start -a android.intent.action.VIEW -d https://github.com/BlackHydra40/BlackBIN > /dev/null 2>&1
sleep 5
clear
figlet "ABRINDO TELEGRAM" | lolcat
am start -a android.intent.action.VIEW -d https://t.me/MS40_canal > /dev/null 2>&1
sleep 3

git clone https://github.com/BlackHydra40/BlackBIN
cd BlackBIN
clear
bash black.sh
