print('Exercitiu 1')
# 1.Funcție care să calculeze și să returneze suma a două numere
def suma(x,y):

    z = x + y
    return z

print(f"Suma celor doua numere este: {suma(3,5)}")

print()
print('Exercitiu 2')
# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

def odd_even_number(x):

    if x % 2 == 0:
        return True
    else:
        return False

print(odd_even_number(4))

print()
print('Exercitiu 3')
"""
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
"""
def name_len(nume, prenume, nume_mijlociu):

    nume_complet = nume + prenume + nume_mijlociu
    return len(nume_complet)

print(name_len('Comsa','Maria','Cristina'))

print()
print('Exercitiu 4')
# 4. Funcție care returnează aria dreptunghiului

def aria_dreptunghiului(latime, lungime):

    aria = latime * lungime
    return aria

print(f"Aria dreptunghiului este {aria_dreptunghiului(3, 6)}")

print()
print('Exercitiu 5')
# 5. Funcție care returnează aria cercului

def aria_cercului(pi, r):

    aria = pi * ( r ** 2 )
    return aria

print(aria_cercului(3.14, 4))

print()
print('Exercitiu 6')
"""
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și False dacă nu găsește.
"""

def get_char(text):

    if 'Buna' in text:
        return True
    else:
        return False

print(get_char('Buna, ce faci?'))

print()
print('Exercitiu 7')
"""
7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
"""

def char_lower_upper(text):
    contor_lower = 0
    contor_upper = 0
    for letter in text:
        if letter.islower():
            contor_lower += 1
        if letter.isupper():
            contor_upper += 1

    print(f'Nr. de caractere lower case este {contor_lower}')
    print(f'Nr. de caractere upper case este {contor_upper}')

char_lower_upper('Buna, ce faci, Geo?')

print()
print('Exercitiu 8')
"""
8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive
"""

def positive_list(my_list):

    my_list_positive = []
    for x in my_list:
        if x >= 0:
            my_list_positive.append(x)
    return my_list_positive

my_list = [2, 3, -1, 5, 0, -6]
print(positive_list(my_list))

print()
print('Exercitiu 9')
"""
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.
"""

def compare_numbers(x,y):
    if x > y:
        print(f" {x} is higher than {y}")
    elif x < y:
        print(f" {x} is lower than {y}")
    else:
        print('The numbers are equals')
x = int(input('Enter x: '))
y = int(input('Enter y: '))

compare_numbers(x, y)

print()
print('Exercitiu 10')
"""
10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
"""
def get_number(x, my_set):

    if x not in  my_set:
        my_set.add(x)
        print(f'I added the new number {x} in the set!')
        return True
    else:
        print(f"I didn't add the number {x}, it is already in the set!")
        return False

print(get_number(9,my_set={1, 3, 4, (2, 5, 7)}))

print()
print('Exercitiu optional 1')
# 1. Funcție care primește o lună din an și returnează câte zile are acea luna

def get_days_of_month(get_month, year):

    year = {'ianuarie': '31', 'februarie': '28/29', 'martie': '31', 'aprilie': '30', 'mai': '31', 'iunie': '30',
              'iulie': '31', 'august': '31', 'septembrie': '30', 'octombrie': '31', 'noiembrie': '30',
              'decembrie': '31'}

    for month, days in year.items():
        if month == get_month:
            return days

print(get_days_of_month(get_month=input('enter a month: '), year={'ianuarie': '31', 'februarie': '28/29', 'martie': '31', 'aprilie': '30', 'mai': '31', 'iunie': '30',
              'iulie': '31', 'august': '31', 'septembrie': '30', 'octombrie': '31', 'noiembrie': '30',
              'decembrie': '31'}))

print()
print('Exercitiu optional 2')
"""
2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
împărțirea a două numere.
În final vei putea face:
a, b, c, d = calculator(10, 2)
● print("Suma: ", a)
● print("Diferenta: ", b)
● print("Inmultirea: ", c)
● print("Impartirea: ", d)
"""

def calculator(x, y):

    a = x + y
    b = x - y
    c = x * y
    d = x / y
    print(f"Suma of {x} and {y} is: {a}")
    print(f"Substraction of {x} and {y} is: {b}")
    print(f"Multiplication of {x} and {y} is: {c}")
    print(f"Division of {x} and {y} is: {d}")

calculator(10, 2)

print()
print('Exercitiu optional 3')
"""
3. Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
"""
def count_list(my_list):
    """returnam frecventa elementelor din lista intr-un dictionar"""

    contor = {}
    for i in my_list:
        if i in contor:
            contor[i] += 1
        else:
            contor[i] =1
    return contor

print(count_list(my_list=[1, 3, 1, 5, 9, 7, 7, 5, 5]))

print()
print("Exercitiu optional 4")
# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
def max_number(x,y,z):

    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z

print(f"numarul mai mare este {max_number(2,3,1)}")

print()
print("exercitiu optional 5")
"""
5. Funcție care să primească un număr și să returneze suma tuturor numerelor
de la 0 la acel număr
Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
"""
def sum_numbers(number):
    """iteram prin numere si returnam suma lor"""

    total = sum(range(0,number+1))

    return total

print(f"suma numerelor este={sum_numbers(5)}")

print()
print('Exercitiu bonus 1')
"""1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
numerele comune
"""
def numere_comune(l1, l2):
    l1 = set(l1)
    l2 = set(l2)
    z = l1.intersection(l2)
    return z

print(numere_comune(l1=[1, 1, 2, 3, 4, 3],l2=[2, 2, 3, 4, 5] ))

print()
print('Exercitiu bonus 2')
"""
2.. Funcție care să aplice o reducere de preț
Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
invalidă.
"""
def discount_calculator(user_price, user_discount):
    if 0 < user_discount < 100:
        final_price = user_price - user_price * user_discount / 100
        return final_price
    else:
        print("\nThe entered discount is invalid!")


price = float(input("\nEnter the product price to calculate the discount price:\t"))
discount = float(input("\nEnter the discount (%):\t"))
print(f"\nThe final price is: {round(discount_calculator(price, discount), 2)}")
print()

print()
print('exercitiu bonus 3')
"""
3. Funcție care să afișeze data și ora curentă din ro
(bonus: afișați și data și ora curentă din China)
"""
from datetime import datetime
import pytz


def romania_time():
    romania_time_now = datetime.now().time()
    return romania_time_now


def china_time():
    china_timezone = pytz.timezone('Asia/Shanghai')
    china_time_now = datetime.now(china_timezone).time()
    return china_time_now


print(f"\nOra in Romania: {romania_time()}")
print(f"\nOra in China: {china_time()}")

print()
print("Exercitiu bonus 4")
"""
4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
Crăciun dacă nu vrei să ne zici cand e ziua ta :)
"""

def calculator_aniversare(data_aniversare):
    data_curenta = datetime.now()
    data_curenta_string = str(datetime.now())
    if int(data_curenta_string[5:7]) > int(aniversare[0:2]) and int(data_curenta_string[8:10]) > int(aniversare[3:]):
        data_aniversare = data_aniversare + '/2023'
        data_aniversare_ms = datetime.strptime(data_aniversare, "%m/%d/%Y")
        delta = data_aniversare_ms - data_curenta
        return delta.days
    else:
        data_aniversare = data_aniversare + '/2022'
        data_aniversare_ms = datetime.strptime(data_aniversare, "%m/%d/%Y")
        delta = data_aniversare_ms - data_curenta
        return delta.days


aniversare = input("\nIntrodu data aniversarii tale (ll/zz):\t")
print(f"\nMai sunt {calculator_aniversare(aniversare)} zile pana la ziua ta")
print()





















