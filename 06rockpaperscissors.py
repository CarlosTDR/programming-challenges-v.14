import random
print "Rock Paper Scissors\n G A M E";

victorias = 0;
derrotas = 0;
var = 1;
array = ["nada","piedra","papel","tijeras"];
while var == 1:
    print "";
    print
    tirada = int(raw_input("\nIntroduce your movement: \n 1-Rock\n 2-Paper\n 3-Scissors"));
    maquina = random.randint(1,3);

    print "\nTu tirada es %s y la maquina tira %s" %(array[tirada], array[maquina]);

    if tirada - maquina == -2:  print 'Ganas'; victorias = victorias + 1;
    elif tirada - maquina == 2:  print "Pierdes"; derrotas = derrotas + 1;
    elif tirada - maquina == (1):  print "Ganas"; victorias = victorias + 1;
    elif tirada - maquina == -1:  print "Pierdes";  derrotas = derrotas + 1;
    elif tirada - maquina == 0: print "Empate";

    print "Vas %d a %d contra la maquina" %(victorias, derrotas);
