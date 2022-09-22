<?php
/*Color*/
$verde = "\033[32m";
$rojo = "\033[31m";
$celeste = "\033[36m";
$amarillo = "\033[33m";
$morado = "\033[35m";
$azul = "\033[34m";
$plomo = "\033[30m";

/*Form*/
$date   = date('d-M-Y H:i');
sleep(2);

echo $amarillo. "	           
           ————————————————————————————————————————
             |   ★MS40★   |
           ————————————————————————————————————————\n";
 echo "==================================================================";
echo "\n
\033[01;31m[★] CRIADO POR \033[01;32;1m@ms4010 (Telegram)\033[01;31m\n";
sleep(1);
echo "\033[01;31m[★] PROIBIDO A VENDA DESSA FERRAMENTA\n";
sleep(1);
echo $amarillo. "\n————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————";

//QUATIDADE DE CC

echo $celeste . "\n\nQUANTAS CC VC QUER QUE SEJA GERADA? :  ";
$count = trim(fgets(STDIN,1024));

//GEARANDO CC

for($x = 0; $x < $count; $x++){
$str = file_get_contents("http://namegenerators.org/fake-name-generator-us/");
$var = '/<div class="col2">(.*?)<\/div>/s';
preg_match_all($var, $str, $matches);

// INFORMAÇÕES DE DESTINO

sleep(5);
echo "\033[33m%%%%%%%%%\033[34m%%%%%%%\033[31m%%%%%%\033[32m GERANDO CARTÃO \033[33m%%%%%%%%%\033[01;34m%%%%%%%\033[31m%%%%%%\n";

echo $rojo . "\n=================== INFORMAÇÕES DO USUÁRIO ======================\n\n";
echo $verde . "[NOME : ".str_replace("</span>", "", str_replace('<span class="name">', "", $matches[1][3]))."]".
		" \n[LUGAR : ".$matches[1][8]."]".
		" \n[CORREIO : ".$matches[1][10]."]".
		" \n[TELEFONE : ".$matches[1][9]."]\n";
echo $rojo . "====================== CARTÃO DE CRÉDITO  =======================\n\n";
echo $azul . " \n[CARTÃO DE CRÉDITO : ".str_replace(" ", "", $matches[1][14])."]".
		" \n[CVV : ".$matches[1][16]."]".
		" \n[VENCIMENTO : ".$matches[1][15]."]\n\n";
	sleep(5);
}
echo ">  CC GERADAS, VOLTE SEMPRE MEU MESTRE <3 : " .$plomo .$date."\n";
?>
