# coding=utf-8
import random

print "\nAMIGO INVISIBLE\n"

print "Inserta jugadores";

lista = [];
elegidos = [];

eleccion = True;
while eleccion:
    aux = raw_input("> ");
    if aux == "done":
        break;
    else:
        lista.append(aux);

elegidos.extend(lista);


for i in range(len(lista)):
    trump = True;
    aux = lista[i];
    print u"¿Eres %s y estás en un sitio seguro?" % aux;
    if raw_input("> ") == "si":
        if len(elegidos) > 2:
            if lista[i] in elegidos:
                elegidos.remove(aux);
                trump = True;
            elegido = elegidos[random.randint(0,len(elegidos) - 1)];
            print "Tu amigo es... %s " % elegido
            elegidos.remove(elegido);
            if (trump == True):
                elegidos.append(aux);
        else:
            print "Tu amigo es %s " % elegidos[0];
            elegidos.remove(elegidos[0]);
