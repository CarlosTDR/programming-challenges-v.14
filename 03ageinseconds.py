# -*- coding: utf-8 -*-
import time

print "\nAGEINSECONDS... the hard way\n"

print "Today is ... " + time.strftime("%d\\%m\\%Y")

actualday = int(time.strftime("%d"))
actualmonth = int(time.strftime("%m"))
actualyear = int(time.strftime("%Y"))

print "When you were born?"
print "Set the day:",
birthday = int(raw_input())
print "Set the month:",
birthmonth = int(raw_input())
print "Set the year:",
birthyear = int(raw_input())

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
        if i%4 == 0 and (not(i%100 == 0) or i%400 == 0):
            res = res + 1
    return res

totaldays = float(years*360 + months * 31 + days +
bisiestos(birthyear,actualyear))
totalsec = float(totaldays*24*3600)

print "\nLlevas vividos... "
print "%d years %d months and %d days" % (years,months,days)
print "lo que equivale a %fs de misera existencia" % totalsec
