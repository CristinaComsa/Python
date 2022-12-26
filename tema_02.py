# Exercitiu 1
"""
if else = prin if, else se verifica o conditie de adevar, daca prima conditie  este adevarata
se executa expresiile din codul If, iar daca nu este adevarata, se ruleaza  expresiile din codul else..
"""
import re

# Exercitiu 2 , daca x este numar natural
x = int(input('Introduceti un numar: '))
if x >= 0:
    print('x este numar natural')
else:
    print('x nu este numar natural')
print()

# Exercitiu 3, daca x este pozitiv, negativ sau neutru
x = int(input('Introduceti un numar: '))
if x == 0:
    print('x este numar neutru')
elif x > 0:
    print('x este numar pozitiv')
else:
    print('x este numar negativ')
print()

# Exercitiu 4, verifica daca x este intre -2 si 13
x = int(input('Introduceti un numar intre -2 si 13: '))
if x >= -2 and x <= 13:
    print(x)
else:
    print('Numarul nu este intre -2 si 13')
print()

# Exercitiu 5, verifica daca diferenta dintre x si y < 5
x = int(input('Introduceti x: '))
y = int(input('Introduceti y: '))
z = x - y
if z < 5:
    print('Diferenta dintre  x si y este: ', z)
else:
    print('Diferenta dintre x si y este > 5!')
print()

# Exercitiu 6, verific daca x nu este intre 5 si 27 NOT
x = int(input('Introduceti un numar: '))
if not x in range(5, 28):
    print(x)
else:
    print('Numarul este intre 5 si 27.')
print()

# Exercitiu 7, verific daca x = y, daca nu, afisez care e mai >
x = int(input('Introduceti x: '))
y = int(input('Introduceti y: '))
if x == y:
    print('x si y sunt egale!')
elif x > y:
    print('x > y')
else:
    print('x < y')
print()

# Exercitiu 8, x, y, z = laturile unui triunghi, triunghi isoscel, echilateral sau oarecare
x = int(input('introduceti x latura unui triunghi: '))
y = int(input('introduceti y latura unui triunghi: '))
z = int(input('introduceti z latura unui triunghi: '))
if x != y and y != z and x != z:
    print('Triunghi oarecare.')
elif x == y == z:
    print('Triunghi echilateral!')
elif y == z or x == y or x == z:
    print('Triunghi isoscel!')
else:
    print('Triunghi necomform :)')
print()

# Exercitiu 9, a se verifica si afisa daca litera cittita este o vocala
litera = input(('Introduceti o litera: '))
if litera in ('a, e, i, o, u, A, E, I, O , U'):
    print('Litera aleasa este o vocala!')
else:
    print('Litera aleasa este o consoana!')
print()

# Exercitiu 10, transform notele din sistem romanesc in note
nota = float(input('Introduceti nota: '))
if nota > 9 and nota <= 10:
    print('A')
elif nota > 8 and nota <= 9:
    print('B')
elif nota > 7 and nota <= 8:
    print('C')
elif nota > 6 and nota <= 7:
    print('D')
elif nota > 4 and nota <= 6:
    print('E')
elif nota <= 4 and nota > 0:
    print('F')
else:
    print('Nota nu se incadreaza in sistemul romanesc de notare!')
print()

# Exercitiu 1 - optional , verifica daca x are minim 4 cifre...
x = (input('Introduceti un numar din 4 cifre: '))
lungime_x = int(len(x))
if lungime_x >= 4:
    print(x)
else:
    print('Numarul are mai putin de 4 cifre.')
print()

# Exercitiu 2 - optional, daca numarul are exact 6 cifre
x = int(input('introduceti un numar din 6 cifre: '))
if 1 <= x/100000 < 10:
    print(x)
else:
    print('Numarul introdus nu are 6 cifre.')
print()

# Exercitiu 3 - optional, sa verific daca x este par sau impar
x = int(input('Introduceti un numar: '))
if x % 2 == 0:
    print('Numarul este par.')
else:
    print('Numarul este impar.')
print()

# Exercitiu 4 - optional, x, y, z = afisam pe cel mai mare
x = int(input("introduceti x: "))
y = int(input("introduceti y: "))
z = int(input("introduceti z: "))
if x > y > z:
    print(x)
elif y > x > z:
    print(y)
else:
    print(z)
print()

#  Exercitiu 5 - optional, x,y,z - unghiurile unui triunghi--> verific daca triunghiul e valid sau nu
x = (int(input('Introduceti x ca unghi a unui triunghi: ')))
y = (int(input('Introduceti y ca unghi a unui triunghi: ')))
z = (int(input('Introduceti z ca unghi a unui triunghi: ')))
if x + y + z == 180 and x > 0 and y > 0 and z > 0:
    print('Triunghiul este valid.')
else:
    print('Triunghiul nu este valid!')
print()

# Exercitiu 6 - optional, se da textul si trebuie citit fara numarul de caractere ales de la tastatura
text = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Introduceti un numar: '))
print(text[0:-x])
print()

# Exercitiu 7 - optional, acelasi text , sa se afiseze primul+ultimul cuvant
text = 'Coral is either the stupidest animal or the smartest rock'
cuv_1 = text[0:5]
cuv_2 = text[-5:]
print(cuv_1 + cuv_2)
print()

# Exercitiu 8 - optional, acelesi text, salvez intr-o variabila indexul de start, apoi slicing..
text = 'Coral is either the stupidest animal or the smartest rock'
idx_cuv = text.index('rock')
print(idx_cuv)
print(text[0:idx_cuv])
print()

# Exercitiu 9 - optional, se citeste un string, se verifica primul si ultimul caracter sa fie la fel, case insensitive
txt = input('Introduceti un cuvant: ')
assert txt[0].upper() == txt[-1].upper(), 'nu sunt la fel'

# Exercitiu 10 - optional, se da stringul, sa se afiseze numerele impare apoi cele pare
str = '0123456789'
str_par = str[0::2]
str_impar = str[1::2]
print(f'Numerele pare sunt {str_par}')
print(f'Numerele impare sunt {str_impar}')
print()

# Exercitiu 11 - optional, ghiceste zarul!
import random
dice_roll = random.randint(1, 6)
zar_ghicit = input('Ghiceste numar zar: ')
if zar_ghicit in ['1', '2', '3', '4', '5', '6']:
    if int(zar_ghicit) < int(dice_roll) and int(zar_ghicit) >= 1:
        print(f'Ai pierdut! Numarul {zar_ghicit} < {dice_roll}')
    elif int(zar_ghicit) > int(dice_roll) and int(zar_ghicit) <= 6:
        print(f'Ai pierdut! Numarul ales {zar_ghicit} > {dice_roll}')
    elif int(zar_ghicit) == int(dice_roll):
        print(f'Ai ghicit! Numarul ales {zar_ghicit} = {dice_roll}')
    else:
        print('Numarul ales nu este pe zar!')
else:
    print('Nu esti in jocul corect! Alege un zar intre 1 si 6!')





