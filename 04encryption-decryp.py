
print "Codificando";

txt_string = raw_input("Intruce tu texto: ");
result = [];

def encriptar (c):
    temp = ord(c);
    temp = temp + key;
    return chr(temp);

key = int(raw_input("Introduce tu clave: "));
for letter in txt_string:
        result.append(encriptar(letter));

res = "".join(result);

print "Codificado: '%s'" % res;
