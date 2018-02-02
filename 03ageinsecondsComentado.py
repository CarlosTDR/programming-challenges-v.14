# -*- encoding: utf-8 -*-
import time

print "AGEINSECONDS... the hard way\n"

print "Today is ... " + time.strftime("%d\\%m\\%Y")

actualday = int(time.strftime("%d"))
actualmonth = int(time.strftime("%m"))
actualyear = int(time.strftime("%Y"))

print "When you where born?"
# Más bonito, aparte el print con una coma al final funcion de una forma un
# tanto especial.
#raw_input() te devuelve una cadena de carácteres
#int(raw_input()) aquí es redundante

birthday = input("Day: ")
birthmonth = input("Month: ")
birthyear = input("Year: ")

years = actualyear - birthyear
months = actualmonth - birthmonth
days = actualday - birthday

if days < 0:
    days = 31 + days
    months = months - 1
if months < 0:
    months = 12 + months
    years = years - 1
if years <= 0:
    print "Aun no has nacido, subnormal"

def bisiestos(i,j):
    res = 0
    for i in range(i,j):
        # es mejor "X != Y" que "not X == Y"
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            # puedes utilizar += 1
            res += 1
    return res

# no todos los meses tienen 31 dias
# un año tiene 365,25 días, no 360
totaldays = float(years*365.25 + months * 31 + days + bisiestos(birthyear,actualyear))
totalsec = float(totaldays*24*3600)

print "\nLlevas vividos... "
print "%d years %d months and %d days" % (years,months,days)
print "lo que equivale a %f s de misera existencia" % totalsec
