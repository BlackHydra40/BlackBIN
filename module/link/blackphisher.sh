# Bash Script for Hide Phishing URL Created by KP

url_checker() {
    if [ ! "${1//:*}" = http ]; then
        if [ ! "${1//:*}" = https ]; then
            echo -e "\e[31m[!] URL INVALIDA. PRECISA CONTER http OU https!!\e[0m"
            exit 1
        fi
    fi
}

cd cat
cat bp.txt | lolcat
echo -e "\e[40;38;5;82m VISITE O NOSSO CANAL \e[30;48;5;82m https://t.me/MS40_canal \e[0m"
echo -e "\e[30;48;5;82m    Copyright \e[40;38;5;82m ms40[Black-hydra] \e[0m \n\n"
echo -e "\e[30:48:5:82m    MEU PIX PARA DOAÇÕES: maycongg486@gmail.com \e[0m \n\n"
echo -e "\e[1;31;42m ### URL ###\e[0m \n"
echo -n "Cole a sua URL maliciosa aqui (ex: http or https): "
read phish
url_checker $phish
sleep 1
echo "Processando e Modificando URL..."
echo ""
short=$(curl -s https://is.gd/create.php\?format\=simple\&url\=${phish})
shorter=${short#https://}
echo -e "\n\e[1;31;42m ### DOMÍNIOS ###\e[0m"
echo 'Escolha um Domínio para ter na URL Phishing!! (use http ou https), ex: https://google.com, http
://anything.org) :'
echo -en "\e[32m=>\e[0m "
read mask
url_checker $mask
echo -e '\nDigite palavras de engenharia social:(como dinheiro grátis e sites de porno)'
echo -e "\e[31mUse espaço apenas colocando  -  entre palavras de engenharia social \e[0m"
echo -en "\e[32m=>\e[0m "
read words
if [[ -z "$words" ]]; then
echo -e "\e[31m[!] Sem palavras.\e[0m"
echo -e "\nGenerando Link modificado...\n"
final=$mask@$shorter
echo -e "Aqui está o URL do BlackPhisher:\e[32m ${final} \e[0m\n"
exit
fi
if [[ "$words" =~ " " ]]; then
echo -e "\e[31m[!] Palavras inválidas. Por favor, evite espaço.\e[0m"
echo -e "\nGenerando Link modificado...\n"
final=$mask@$shorter
echo -e "Aqui está o URL do BlackPhisher:\e[32m ${final} \e[0m\n"
exit
fi
echo -e "\nGenerando Link modificado...\n"
final=$mask-$words@$shorter
echo -e "Aqui está o URL do BlackPhisher:\e[32m ${final} \e[0m\n"
