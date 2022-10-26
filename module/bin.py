from random import randint
import datetime
import random
import os
import sys
import time
##By: MS40
##telegram @ms4010
##meu pix: maycongg486@gmail.com

#COLORES
rojo = '\033[31;1m'
azul = '\033[34;1m'
verde = '\033[32;1m'
amarillo = '\033[33;1m'
morado = '\033[35;1m'
celeste = '\033[36;1m'
plomo = '\033[30;1m'
close = '\033[0m'

os.system("clear")
print("!!AVISO!!")
print("USE ESSA FERRAMENTA COM SUA CONTA EM RISCO")
print("NÃO SOMOS RESPONSAVEL PELO OQUE VC FAZ >:(")
time.sleep(4)
print("ABRINDO CANAL DO TELEGRAM...")
time.sleep(1)
os.system("xdg-open https://t.me/MS40_canal")
time.sleep(1)

os.system("clear")
os.system ("toilet -f big 'NICK' -F gay | lolcat")
print(amarillo)
nick = str(input(' COLOQUE SEU NICK  : '))
os.system("clear")
os.system ("toilet -f big '★ MS40★' -F gay | lolcat")
os.system ("toilet -f big '★ KUROKO★' -F gay | lolcat")
time.sleep(3)
os.system("clear")
os.system ("toilet -f big '★SEJA★' -F gay | lolcat")
os.system ("toilet -f big '★BEM VINDO★' -F gay | lolcat")
time.sleep(3)
os.system("clear")
os.system ("toilet -f big 'BLACKBIN' -F gay | lolcat")
print("\n\033[33;1m OLÁ \033[31;1m★",nick,"★\033[33;1m BEM VINDO AO BLACK_BIN\n")
print("\033[31;1m         MEU CANAL DO TELEGRAM: MS40_canal \033[32;1m")
print("\033[34;1m         CRIADO POR MS40 \033[32;1m")
print("MEU PIX: maycongg486@gmail.com ")
print('---------------------------------------------------------')
time.sleep(1)
s = True
n = False
list = [2023, 2024, 2025, 2026, 2022, 2027]
nume = random.randrange(1, 9999999999999999)
cvv = random.randint(3, 999)
data1 = random.randrange(1, 31)
data2 = random.randrange(1, 12)
data3 = random.choice(list)
cpf = random.randrange(1, 99999999999)

bi = str(input('Você deseja inserir sua BIN e concorda com o termo de uso ? s ou n?: '))

if bi == 's':
    nume2 = random.randrange(1, 9999999999)
    bin = int(input('Digite sua BIN de 6 digitos : '))
    print('Número do cartão', bin, nume2)
    print('Cvv do cartão:',cvv)
    print('Data do cartão:', data1, data2, data3)
    print('CPF cadastrado no cartão:', cpf)
    
else:
    time.sleep(1)  
    print("\033[33;1m não é possivel iniciar a ferramenta. (termo de uso negado!!!) \033[32;1m")

