import random
print "Higher/lower\nG A M E";

print "\nI'm think a number... \nDONE.\n";

random = random.randint(0,100);
print "Now guess\n"
var = 0;
while var == 0:

    chose = int(raw_input());
    if chose == random:
        print "Correcto"
        var = 1;
        break;
    elif chose > random:
        print "Abajo";
    else:
        print "Arriba";
