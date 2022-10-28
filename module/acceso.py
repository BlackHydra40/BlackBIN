import os
import sys
import time

#COLORES
rojo = '\033[31;1m'
azul = '\033[34;1m'
verde = '\033[32;1m'
amarillo = '\033[33;1m'
morado = '\033[35;1m'
celeste = '\033[36;1m'
plomo = '\033[30;1m'
close = '\033[0m'


username = 'BLACKHYDRANGKS'      
password = '1012'


print(amarillo)
os.system ("toilet -f big 'NICK' -F gay | lolcat")
nick = str(input(' COLOQUE SEU NICK  : '))

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = str(input("\n\033[33;1mUSUARIO : \033[32;1m"))
	if uname == username:
		pwd = str(input("\n\033[33;1mSENHA : \033[32;1m"))

		if pwd == password:
			os.system("clear")
			time.sleep(2)
            #printf "\e[1;34m Abrindo canal no Telegram \n\e[m" && xdg-open https://t.me/MS40_canal &> /dev/null && sleep 10
			os.system ("toilet -f big 'BlackBIN' -F gay | lolcat")
			print("\n\033[32;1m OLÁ \033[32;1m ★",nick,"★\033[32;1m BEM VINDO AO BLACKBIN \n  FERRAMENTO VOLTADO A CC, GERADORES E BINS\n")
			time.sleep(2)
			print(verde,'+————————————————————————————————————————————————————————————+')
			print(verde)
			print('  [ 01 ] CARTÕES DO ESTADOS UNIDOS')
			print('  [ 02 ] CARTÕES DA AUSTALIA')
			print('  [ 03 ] CARTÕES DA AUSTRIA')
			print('  [ 04 ] CARTÕES DA BÉLGICA')
			print('  [ 05 ] CARTÕES DO BRASIL')
			print('  [ 06 ] CARTÕES DO CANADA')
			print('  [ 07 ] CARTÕES DA DINAMARCA')
			print('  [ 08 ] CARTÕES DA ESTONIA')
			print('  [ 09 ] CARTÕES DA FINLANDIA')
			print('  [ 10 ] CARTÕES DA FRANÇA')
			print('  [ 11 ] CARTÕES DA ALEMANHA')
			print('  [ 12 ] CARTÕES DA GROELÃNDIA')
			print('  [ 13 ] CARTÕES DE HUNGARYA')
			print('  [ 14 ] CARTÕES DA ISLÃNDIA')
			print('  [ 15 ] CARTÕES DA HOLANDA')
			print('  [ 16 ] CARTÕES DA NORUEGA')
			print('  [ 17 ] CARTÕES DA POLÔNIA')
			print('  [ 18 ] CARTÕES DE PORTUGAL')
			print('  [ 19 ] CARTÕES DA ESLOVÊNIA')
			print('  [ 20 ] CARTÕES DA ESPANHA')
			print('  [ 21 ] CARTÕES DA SUÉCIA')
			print('  [ 22 ] CARTÕES DA SUÍÇA')
			print('  [ 23 ] CARTÕES DA TUNÍSIA')
			print('  [ 24 ] REDES SOCIAIS E SOBRE\n\033[31;1m')
			sys.exit()
			

		else:
			os.system("clear")
			print("\n\033[1;31m SINTO MUITO " , nick, " O USUARIO OU SENHA ESTA INCORRETO !!!\033[00m")
			print(azul, "MEU CONTATO PARA AJUDA @ms4010 (telegram)")
			time.sleep(3.3)
			os.system("clear")
			restart()

	else:
		os.system("clear")
		print("\n\033[1;31m SINTO MUITO " , nick, " O USUARIO OU SENHA ESTA INCORRETO !!!\033[00m")
		print(azul, "\nMEU CONTATO PARA AJUDA @ms4010 (telegram)")
		time.sleep(3.3)
		os.system("clear")
		restart()

try:
	main()
except KeyboardInterrupt:
       print(azul, "\n\033[34;1m [!] Ctrl+C precionado, BlackCCV8 interrompido!\033[00m")
