clear
cd
rm -rf $HOME/BlackBIN
figlet "ATUALIZANDO" | lolcat
figlet "AGUARDE..." | lolcat
echo "saiba mais sobre novas atalizações e noticias"
echo "https://github.com/BlackHydra40/BlackBIN"
echo

git clone https://github.com/BlackHydra40/BlackBIN
cd BlackBIN
clear
bash blackv8.sh

sleep 3
