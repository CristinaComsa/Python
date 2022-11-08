import datetime
from tabulate import tabulate


print('exercitiu 1')
"""
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
"""
class Cerc:
    def __init__(self,raza,culoare):
        self._raza = raza
        self._culoare = culoare

    def descrie_cerc(self):
        print(f"Raza cercului este {self._raza} si are culoarea {self._culoare}")

    def aria(self):
        aria = 3.14 * self._raza ** 2
        return aria

    def diametru(self):
        diametru = 2*self._raza
        return diametru

    def circumferinta(self):
        circumferinta = 2 * 3.14 * self._raza
        return circumferinta

cerc1 = Cerc(10, 'red')
cerc1.descrie_cerc()
print(cerc1.aria())
print(cerc1.diametru())
print(cerc1.circumferinta())
cerc2 = Cerc(4, 'green')
cerc2.descrie_cerc()
print(cerc2.aria())
print(cerc2.diametru())
print(cerc2.circumferinta())

print()
print('Exercitiu 2')
"""
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
"""


class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self._lungime = lungime
        self._latime = latime
        self._culoare = culoare

    def descriere(self):
        print(f"Dreptunghiul are lungimea {self._lungime}, latimea {self._latime} si culoarea {self._culoare}")

    def aria(self):
        aria = self._lungime * self._latime
        return aria

    def perimetru(self):
        perimetru = 2 * (self._lungime * self._latime)
        return perimetru
    def schimba_culoare(self,culoare):
        self._culoare = culoare

dreptunghi1 = Dreptunghi(10, 6, 'Red')
dreptunghi1.descriere()
print(f"Aria={dreptunghi1.aria()}")
print(f"Perimetru={dreptunghi1.perimetru()}")
dreptunghi1.schimba_culoare('Green')
dreptunghi1.descriere()
print()
dreptunghi2 = Dreptunghi(5, 8, 'Blue')
dreptunghi2.descriere()
print(f"Aria={dreptunghi2.aria()}")
print(f"Perimetru={dreptunghi2.perimetru()}")
dreptunghi2.schimba_culoare('Yellow')
dreptunghi2.descriere()

print()
print('Exercitiu 3')
"""
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
"""
class Employee:
    def __init__(self, name,surname,salary):
        self._name = name
        self._surname = surname
        self._salary = salary

    def description(self):
        return print(f"My name is {self._name} {self._surname}")

    def complete_name(self):
        return self._name + " " + self._surname

    def month_salary(self):
        return self._salary

    def anual_salary(self):
        return self._salary * 12

    def pay_raise(self,procent):
        procent = self._salary / 300
        return procent


employee1 = Employee('Rus', 'Ana', 3000)
employee1.description()
print(f"My entire name is {employee1.complete_name()}")
print(f"My mounthly salary is {employee1.month_salary()}")
print(f"My anual salary is {employee1.anual_salary()}")
print(f"My pay raise is {employee1.pay_raise(10)} procent")
print()
employee2 = Employee('Pop', 'Marius', 4000)
employee2.description()
print(f"My entire name is {employee2.complete_name()}")
print(f"My mounthly salary is {employee2.month_salary()}")
print(f"My anual salary is {employee2.anual_salary()}")
print(f"My pay raise is {employee2.pay_raise(10)} procent")
print()
print('Exercitiu 4')
"""
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
"""
class BankAccount:
    def __init__(self,iban,account_holder,sold):
        self._iban = iban
        self._account_holder = account_holder
        self._sold = sold

    def get_sold(self):
       print(f"Welcome, {self._account_holder}!")
       print(f"Your current balance is {self._sold}")

    def account_debit(self):
        print(f"Please enter the money!")
        debit_sold = 300
        self._sold = self._sold + debit_sold
        return self._sold

    def account_credit(self):
        credit_sold = int(input('How much credit do you want to withdraw?\n'))
        if credit_sold >=0 and credit_sold <= self._sold:
            return print(f'Your current balance is {self._sold - credit_sold}')
        else:
            return print('Insufficient funds!')

my_account_1 = BankAccount('RO60','Maria Pop', 3000)
my_account_1.get_sold()
print(f"current_sold after debit  = {my_account_1.account_debit()}")
my_account_1.account_credit()
print()
my_account_2 = BankAccount('RO80','Gabriel Popescu', 5000)
my_account_2.get_sold()
print(f"current_sold after debit  = {my_account_1.account_debit()}")
my_account_2.account_credit()

print()
print('Exercitiu optional 1')
"""
1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7        | 700         | 49000
"""
class Factura:

    def __init__(self, numar, nume_produs, cantitate, pret_bucata, serie="FF"):
        self._numar = numar
        self._nume_produs = nume_produs
        self._cantitate = cantitate
        self._pret_bucata = pret_bucata
        self._serie = serie

    def schimba_cantitate(self, cantitate):
        self._cantitate = cantitate

    def schimba_pret(self, pret_bucata):
        self._pret_bucata = pret_bucata

    def schimba_nume_produs(self, nume_produs):
        self._nume_produs = nume_produs

    def generare_factura(self):
        factura_header = [['Factura fiscala   ', f'Seria: {self._serie}    ', f'Numar: {self._numar}'],
                          ['------------------------------------------'],
                          [f'Data: {datetime.date.today()}'],
                          ['------------------------------------------']
                          ]
        factura = [[self._nume_produs, self._cantitate, self._pret_bucata, self._cantitate * self._pret_bucata]]
        print('------------------------------------------')
        for item in factura_header:
            print(*item)
        print(tabulate(factura, headers=['Produs', 'Cantitate', 'Pret/buc', 'Total']))
        print('------------------------------------------')
        print('*' * 80)
        print()


produs_1 = Factura('100', 'Telefon', 2, 300)
produs_1.generare_factura()
produs_1.schimba_nume_produs('Radio')
produs_1.schimba_cantitate(10)
produs_1.schimba_pret(100)
produs_1.generare_factura()

print()
print('Exercitiu optional 2')
"""
2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0
"""
class Car:
    marca = 'BMW'
    viteza_actuala = 0
    culoare ='Gri'
    culori_disponibile = set(('Rosu','Albastru','Negru','Galben','Alb'))
    inmatriculata = False

    def __init__(self,model,viteza_maxima):
        self._model = model
        self._viteza_maxima = viteza_maxima

    def descriere(self):
        print(f"Fabrica produce masina marca {masina_1.marca}, modelul {self._model}, vine in culoarea {masina_1.culoare},"
              f"ating viteza maxima de {self._viteza_maxima} km/ora, si nu sunt inmatriculate {masina_1.inmatriculata}.")
    def inmatriculare(self):
        if masina_1.inmatriculata == True:
            return f"Masina {self._model}nu este inmatriculata"
        else:
            masina_1.inmatriculata = False
            return f"Masina {self._model} este inmatriculata"

    def vopseste(self,culoare):
        culoare = culoare
        masina_1.culori_disponibile = list(masina_1.culori_disponibile)
        if culoare in masina_1.culori_disponibile:
            print(f'Ai ales culoarea potrivita, {culoare}!')
        else:
            print('Ne pare rau, momentan nu avem aceasta culoare disponibila!')

    def accelerare(self,viteza):
        viteza = viteza
        if viteza > 0 and viteza <= self._viteza_maxima:
            return print(f'Viteza = {viteza}\nVrum Vrum Vrum')
        elif viteza == 0:
            print('Masina stationeaza')
        elif viteza > self._viteza_maxima:
            print(f'Viteza maxima este {self._viteza_maxima}!')
        elif viteza < 0:
            return print('Error! va rugam accelerati')

    def franeaza(self):
        print(f'Stop! viteza= {masina_1.viteza_actuala}')


masina_1 = Car('X5',170)
masina_1.descriere()
print(Car.inmatriculare(masina_1))
masina_1.vopseste('Rosu')
masina_1.accelerare(10)
masina_1.franeaza()
print('--------------------------------------------------------------------------------------------------------------')
masina_2 = Car('X7',180)
masina_2.descriere()
print(Car.inmatriculare(masina_2))
masina_2.vopseste('Violet')
masina_2.accelerare(20)
masina_2.franeaza()

print()
print('Exercitiu optional 3')
"""
3. Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:
● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict
"""
class TodoList:
    todo = dict(())

    def adauga_task(self):
        TodoList.todo.update({'ora 8:00': 'sedinta','ora 12:00': 'intalnire afaceri','ora 18:00':'relaxare'},)
        return TodoList.todo
    def finalizeaza_task(self):
        finalizat = TodoList.todo.pop("ora 8:00")
        print(f'Am finalizat taskul {finalizat}.')
        return TodoList.todo
    def afiseaza_todo_list(self):
        for task in TodoList.todo.keys():
            print(f"task: {task}")
    def afisare_detalii(self):
        for descriere in TodoList.todo.values():
            print(f"descriere: {descriere}")



todo = TodoList()
print(todo.adauga_task())
print(f"Taskuri ramase= {todo.finalizeaza_task()}")
todo.afiseaza_todo_list()
todo.afisare_detalii()




